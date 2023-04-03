import sys 
import io 
import opcode
import uuid 
import csv 
import json 
csvFileName ="algoData656b770e-506f-4b07-9dbf-113a0fa4bbaf.csv" 
with open (csvFileName, 'w', newline='') as f: 
    fieldnames = ['event', 'arg', 'line', 'lasti', 'opcode', 'localObjects'] 
    writer = csv.writer(f) 
    writer.writerow(fieldnames) 
def show_trace(frame, event, arg):
    frame.f_trace_opcodes = True
    code = frame.f_code
    offset = frame.f_lasti
    print(f"| {event:10} | {str(arg):>4} |", end=' ')
    print(f"{frame.f_lineno:>4} | {frame.f_lasti:>6} |", end=' ')
    print(f"{opcode.opname[code.co_code[offset]]:<18} | {str(frame.f_locals):<35} |")
    localObjects = {} 
    for key, value in frame.f_locals.items(): 
       localObjects[key] = str(value) 
    localObjects = json.dumps(localObjects) 
    with open(csvFileName, 'a', newline='') as f: 
       writer = csv.DictWriter(f, fieldnames=fieldnames) 
       writer.writerow({'event': event, 'arg': arg, 'line': frame.f_lineno, 'lasti': frame.f_lasti, 'opcode': opcode.opname[code.co_code[offset]], 'localObjects': localObjects}) 
    return show_trace
user_input = "4\n1 1\n3 2\n4 1\n5 3\n" 
saved_stdin = sys.stdin 
sys.stdin = io.StringIO(user_input) 
sys.settrace(show_trace) 
def newFunction():
    # cook your code here
    # cook your code here
    for _t in range(int(input())):
        n,k = map(int, input().split(" "))
        result = []
        if n>1 and k==1:
            print ("-1")
        else:
            for i in range(n):
                result.append(i+1)
            dis = n-k
            result[n-1], result[k-1] = result[k-1], result[n-1]
            output = ""
            for _x in result:
                output += str(_x) + " "
            print (output[:len(output)-1])
            
newFunction() 

sys.settrace(None) 
sys.stdin = saved_stdin 
