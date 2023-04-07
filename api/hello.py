from flask import Flask, request, jsonify
from createCSV import createCSV
from flask_cors import CORS
import csv
import os
import json
import re
import uuid 

p = re.compile('(?<!\\\\)\'')

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    # process body of request
    if request.method == 'POST':
        data = request.get_json()
        # convert data['code'] to .py file
        with open('fucky.py', 'w') as f:
            f.write('from typing import List \n')
            f.write(data['code'])

        csvFileName = createCSV(data['functionName'], data['arguments'])
        print('csvFileName is ', csvFileName)
        # break code into lines based on line break
        codeLines = data['code'].splitlines()
        print('codeLines are ', codeLines)
        visualList = []
        with open(csvFileName, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # check if the line number is valid
                if 2<int(row['line']) < len(codeLines)+3:
                    codeLinePrior = codeLines[int(row['line'])-3]
                    codeLineAt = codeLines[int(row['line'])-2]
                    row['codeLineAt'] = codeLineAt
                    row['codeLinePrior'] = codeLinePrior
                    # convert row['localObjects'] string to dict
                    # row['localObjects'] = json.loads(p.sub('\"', row['localObjects']))
                visualList.append(row)
        
        # if(len(visualList) >0):
        #     os.remove(csvFileName)

        return {'visualList': visualList}


@app.route('/submit-cp', methods=['GET','POST'])
def submitCp():
    data = request.get_json()
    
    csvFileName = "algoData"+str(uuid.uuid4())+".csv"
    # create new python file
    with open('newFile.py', 'w') as f:
        if len(data['importLines']) > 0:
            for line in data['importLines']:
                f.write(line)
                f.write(' \n')
        f.write('import sys \n')
        f.write('import io \n')
        f.write('import opcode\n')
        f.write('import uuid \n')
        f.write('import csv \n')
        f.write('import json \n')
        f.write('csvFileName =')
        f.write('\"'+csvFileName+'\"')
        f.write(' \n')
        f.write('with open (csvFileName, \'w\', newline=\'\') as f: \n')
        f.write('    fieldnames = [\'event\', \'arg\', \'line\', \'lasti\', \'opcode\', \'localObjects\'] \n')
        f.write('    writer = csv.writer(f) \n')
        f.write('    writer.writerow(fieldnames) \n')
        f.write('def show_trace(frame, event, arg):\n')
        f.write('    frame.f_trace_opcodes = True\n')
        f.write('    code = frame.f_code\n')
        f.write('    offset = frame.f_lasti\n')
        f.write('    print(f"| {event:10} | {str(arg):>4} |", end=\' \')\n')
        f.write('    print(f"{frame.f_lineno:>4} | {frame.f_lasti:>6} |", end=\' \')\n')
        f.write('    print(f"{opcode.opname[code.co_code[offset]]:<18} | {str(frame.f_locals):<35} |")\n')
        f.write('    localObjects = {} \n')
        f.write('    for key, value in frame.f_locals.items(): \n')
        f.write('       localObjects[key] = str(value) \n')
        f.write('    localObjects = json.dumps(localObjects) \n')
        f.write('    with open(csvFileName, \'a\', newline=\'\') as f: \n')
        f.write('       writer = csv.DictWriter(f, fieldnames=fieldnames) \n')
        f.write('       writer.writerow({\'event\': event, \'arg\': arg, \'line\': frame.f_lineno, \'lasti\': frame.f_lasti, \'opcode\': opcode.opname[code.co_code[offset]], \'localObjects\': localObjects}) \n') 
        f.write('    return show_trace\n')
        f.write('user_input = "')
        # split data['testCase'] based on line breaks
        testCaseSplit = data['testCase'].splitlines()
        testCaseString = ''
        # add each line to user_input
        for line in testCaseSplit:
            testCaseString += line + '\\n'
        f.write(testCaseString)
        f.write('" \n')
        f.write('saved_stdin = sys.stdin \n')
        f.write('sys.stdin = io.StringIO(user_input) \n')
        f.write('sys.settrace(show_trace) \n')
        # convert data['code'] into a function and write it to file
        f.write('def newFunction():\n')
        # codeLines = data['code'].splitlines()
        for line in data['codeLines']:
            f.write('    ' + line + '\n')
        f.write('newFunction() \n')
        f.write('\n')
        f.write('sys.settrace(None) \n')
        f.write('sys.stdin = saved_stdin \n')

    # run newFile.py
    os.system('python3 newFile.py')

    visualList = []
    codeLines = data['codeLines']
    with open(csvFileName, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # check if the line number is valid
            if 31<int(row['line']):
                try:
                    codeLineAt = codeLines[int(row['line'])-(32+len(data['importLines']))]
                    row['codeLineAt'] = codeLineAt
                except:
                    pass    
               
            visualList.append(row)


    return {'visualList': visualList}

if __name__ == '__main__':
    app.run(host='0.0.0.0')