import opcode  
import sys
import csv

def isMatch(s: str, p: str) -> bool:
        s, p = ' '+ s, ' '+ p
        lenS, lenP = len(s), len(p)
        dp = [[0]*(lenP) for i in range(lenS)]
        dp[0][0] = 1

        for j in range(1, lenP):
            if p[j] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, lenS):
            for j in range(1, lenP):
                if p[j] in {s[i], '.'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})

        return bool(dp[-1][-1])

def show_trace(frame, event, arg):
    frame.f_trace_opcodes = True
    code = frame.f_code
    offset = frame.f_lasti
    
    print(f"| {event:10} | {str(arg):>4} |", end=' ')
    print(f"{frame.f_lineno:>4} | {frame.f_lasti:>6} |", end=' ')
    print(f"{opcode.opname[code.co_code[offset]]:<18} | {str(frame.f_locals):<35} |")


    with open ('algoData.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([event, arg, frame.f_lineno, frame.f_lasti, opcode.opname[code.co_code[offset]], str(frame.f_locals)])

    return show_trace

header = f"| {'event':10} | {'arg':>4} | line | offset | {'opcode':^18} | {'locals':^35} |"

with open ('algoData.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['event', 'arg', 'line', 'offset', 'opcode', 'locals'])


# print(header)
# sys.settrace(show_trace)
# isMatch("aa", "a*")
# sys.settrace(None)

def test(j):
    n = 10
    for i in range(1, n):
        j = i + j
    return j

def createCSV(functionCallString):
    with open ('algoData.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['event', 'arg', 'line', 'offset', 'opcode', 'locals'])

    sys.settrace(show_trace)
    exec(functionCallString)
    sys.settrace(None)
    

