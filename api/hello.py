from flask import Flask, request, jsonify
from createCSV import createCSV
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    # process body of request
    if request.method == 'POST':
        data = request.get_json()
        print(data['test'])
        functionCall = "isMatch('aa', 'a*')"
        createCSV(functionCall)
        return jsonify(data)

    return 'Submit'

if __name__ == '__main__':
    app.run()
