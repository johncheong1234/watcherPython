from flask import Flask, request, jsonify
from createCSV import createCSV
from flask_cors import CORS

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
        print(data)

#         functionCall = s = """
# def test(j):
#     n = 10
#     for i in range(1, n):
#         j = i + j
#     return j

# test(1)
# """

# def isMatch(s: str, p: str) -> bool:
#         s, p = ' '+ s, ' '+ p
#         lenS, lenP = len(s), len(p)
#         dp = [[0]*(lenP) for i in range(lenS)]
#         dp[0][0] = 1

#         for j in range(1, lenP):
#             if p[j] == '*':
#                 dp[0][j] = dp[0][j-2]

#         for i in range(1, lenS):
#             for j in range(1, lenP):
#                 if p[j] in {s[i], '.'}:
#                     dp[i][j] = dp[i-1][j-1]
#                 elif p[j] == "*":
#                     dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})

#         return bool(dp[-1][-1])

        # create a string with multiple lines
        # functionCall = 'def test(j):\n    n = 10\n    for i in range(1, n):\n        j = i + j\n    return j\n\ntest(4)\n'
        # functionCall = data['code']
        functionCall = 'def isMatch(s: str, p: str) -> bool:\n    s, p = \' \' + s, \' \' + p\n    lenS, lenP = len(s), len(p)\n    dp = [[0]*(lenP) for i in range(lenS)]\n    dp[0][0] = 1\n\n    for j in range(1, lenP):\n        if p[j] == \'*\':\n            dp[0][j] = dp[0][j-2]\n\n    for i in range(1, lenS):\n        for j in range(1, lenP):\n            if p[j] in {s[i], \'.\'}:\n                dp[i][j] = dp[i-1][j-1]\n            elif p[j] == "*":\n                dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], \'.\'})\n\n    return bool(dp[-1][-1])\n\nisMatch("aa", "a*")\n'
        print(data['code'])
        createCSV(functionCall)
        return jsonify(data)

    return 'Submit'

if __name__ == '__main__':
    app.run()
