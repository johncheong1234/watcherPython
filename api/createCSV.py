import opcode  
import sys
import csv
import uuid
from typing import List
from fucky import Solution

randomId = uuid.uuid4()
csvFileName = 'algoData' + str(randomId) + '.csv'

def show_trace(frame, event, arg):
    frame.f_trace_opcodes = True
    code = frame.f_code
    offset = frame.f_lasti
    
    print(f"| {event:10} | {str(arg):>4} |", end=' ')
    print(f"{frame.f_lineno:>4} | {frame.f_lasti:>6} |", end=' ')
    print(f"{opcode.opname[code.co_code[offset]]:<18} | {str(frame.f_locals):<35} |")
    # loop through frame.f_locals and print them out:
    localObjects = {}
    for key, value in frame.f_locals.items():

        # implement try catch
        try :
            print(key, value)
            if isinstance(value, (int, float, complex, str, bool, list, tuple, set, dict, frozenset)):
                localObjects[key] = value
        except:
            pass
        

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

def createCSV(functionCallString, arguments):
    argumentString = ''
    for argument in arguments:
        argumentString += str(argument['input'])
        if argument != arguments[-1]:
            argumentString += ','
    #generate a random ID for the csv file
    with open (csvFileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['event', 'arg', 'line', 'offset', 'opcode', 'locals', 'localObjects'])

    sys.settrace(show_trace)
    solution = Solution()
    exec('solution.'+functionCallString+'('+argumentString+')')
    sys.settrace(None)
    return csvFileName
    

