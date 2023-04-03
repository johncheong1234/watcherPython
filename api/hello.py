from flask import Flask, request, jsonify
from createCSV import createCSV
from flask_cors import CORS
import csv
import os
import json
import re

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


@app.route('/submit-cp', methods=['POST'])
def submitCp():
    data = request.get_json()
    
    # create new python file
    with open('newFile.py', 'w') as f:
        
        f.write('import sys \n')
        f.write('import io \n')
        f.write('import opcode\n')
        f.write('def show_trace(frame, event, arg):\n')
        f.write('    frame.f_trace_opcodes = True\n')
        f.write('    code = frame.f_code\n')
        f.write('    offset = frame.f_lasti\n')
        f.write('    print(f"| {event:10} | {str(arg):>4} |", end=\' \')\n')
        f.write('    print(f"{frame.f_lineno:>4} | {frame.f_lasti:>6} |", end=\' \')\n')
        f.write('    print(f"{opcode.opname[code.co_code[offset]]:<18} | {str(frame.f_locals):<35} |")\n')
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
        codeLines = data['code'].splitlines()
        for line in codeLines:
            f.write('    ' + line + '\n')
        f.write('newFunction() \n')
        f.write('\n')
        f.write('sys.settrace(None) \n')
        f.write('sys.stdin = saved_stdin \n')

    return data

if __name__ == '__main__':
    app.run()
