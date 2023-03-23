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
        functionCall = """
# def isMatch(s: str, p: str) -> bool:
#             s, p = ' '+ s, ' '+ p
#             lenS, lenP = len(s), len(p)
#             dp = [[0]*(lenP) for i in range(lenS)]
#             dp[0][0] = 1

#             for j in range(1, lenP):
#                 if p[j] == '*':
#                     dp[0][j] = dp[0][j-2]

#             for i in range(1, lenS):
#                 for j in range(1, lenP):
#                     if p[j] in {s[i], '.'}:
#                         dp[i][j] = dp[i-1][j-1]
#                     elif p[j] == "*":
#                         dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})

#             return bool(dp[-1][-1])

# isMatch('aa', 'a*')
#         """

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
