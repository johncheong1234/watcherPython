import opcode  
import sys
import csv
import uuid
from typing import List

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

randomId = uuid.uuid4()
csvFileName = 'algoData' + str(randomId) + '.csv'

def show_trace(frame, event, arg):
    frame.f_trace_opcodes = True
    code = frame.f_code
    offset = frame.f_lasti
    
    # print(f"| {event:10} | {str(arg):>4} |", end=' ')
    # print(f"{frame.f_lineno:>4} | {frame.f_lasti:>6} |", end=' ')
    # print(f"{opcode.opname[code.co_code[offset]]:<18} | {str(frame.f_locals):<35} |")
    # loop through frame.f_locals and print them out:
    localObjects = {}
    for key, value in frame.f_locals.items():
        print(f"{key}: {value}")
        if isinstance(value, (int, float, complex, str, bool, list, tuple, set, dict)):
            localObjects[key] = value

    with open (csvFileName, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([event, arg, frame.f_lineno, frame.f_lasti, opcode.opname[code.co_code[offset]], frame.f_locals, localObjects])

    return show_trace

header = f"| {'event':10} | {'arg':>4} | line | offset | {'opcode':^18} | {'locals':^35} |"

def test(j):
    n = 10
    for i in range(1, n):
        j = i + j
    return j

def createCSV(functionCallString):
    #generate a random ID for the csv file
    with open (csvFileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['event', 'arg', 'line', 'offset', 'opcode', 'locals', 'localObjects'])

    sys.settrace(show_trace)
    # exec(functionCallString)
#     functionCallString = """
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         cache = {}
#         def rec(s_index, p_index):
#             if (s_index, p_index) in cache: 
#                 return cache[(s_index, p_index)]
            
#             if s_index >= len(s) and p_index >= len(p): 
#                 cache[(s_index, p_index)] = True
#                 return cache[(s_index, p_index)]
            
#             if p_index >= len(p): 
#                 cache[(s_index, p_index)] = False
#                 return cache[(s_index, p_index)]
            
#             match = (s_index < len(s) and p[p_index] in {s[s_index], '.'} )
            
#             if p_index + 1 <len(p) and p[p_index +1] == '*':                
#                 cache[s_index, p_index] = rec(s_index, p_index + 2) or (match and rec(s_index + 1, p_index))               
#                 return cache[s_index, p_index]
            
#             if match:
#                 cache[s_index, p_index] = rec(s_index + 1, p_index+1)
#                 return cache[s_index, p_index]
            
#             cache[s_index, p_index] = False
#             return cache[s_index, p_index]
        
#         return rec(0, 0)

# solution = Solution()
# solution.isMatch("aa", "a*")
#     """
    exec(functionCallString)
    sys.settrace(None)
    return csvFileName
    

