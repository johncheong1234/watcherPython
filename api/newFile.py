import sys 
import io 
import opcode
import uuid 
import csv 
import json 
csvFileName ="algoData1fe16a55-a13f-44e1-89e0-fad3644d2e5b.csv" 
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
user_input = "5\n2\n3\n4\n5\n6\n" 
saved_stdin = sys.stdin 
sys.stdin = io.StringIO(user_input) 
sys.settrace(show_trace) 
def newFunction():
    for _ in range(int(input())):
        n = int(input())
        ans = []
        for x,y in zip(range (n,n//2-1,-1),range(1,n//2+1)):
            ans.append(x)
            ans.append(y)
        else:
            if n%2:
                ans.append(n//2 +1)
        print(*reversed(ans))
newFunction() 

sys.settrace(None) 
sys.stdin = saved_stdin 
