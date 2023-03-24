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
        
#         functionCall = s = """
# def test(j):
#     n = 10
#     for i in range(1, n):
#         j = i + j
#     return j

# test(1)
# """

        # create a string with multiple lines
        functionCall = 'def test(j):\n    n = 10\n    for i in range(1, n):\n        j = i + j\n    return j\n\ntest(4)\n'
        print(functionCall)
        createCSV(functionCall)
        return jsonify(data)

    return 'Submit'

if __name__ == '__main__':
    app.run()
