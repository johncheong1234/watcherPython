from flask import Flask, request, jsonify
from createCSV import createCSV
from flask_cors import CORS
import csv
import os

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

        # break code into lines based on line break
        codeLines = data['code'].splitlines()
        print('codeLines are ', codeLines)
        visualList = []
        with open(csvFileName, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # check if the line number is valid
                if 1<int(row['line']) < len(codeLines):
                    codeLinePrior = codeLines[int(row['line'])-2]
                    codeLineAt = codeLines[int(row['line'])-1]
                    row['codeLineAt'] = codeLineAt
                    row['codeLinePrior'] = codeLinePrior
                visualList.append(row)
        
        if(len(visualList) >0):
            os.remove(csvFileName)
        return {'visualList': visualList}


if __name__ == '__main__':
    app.run()
