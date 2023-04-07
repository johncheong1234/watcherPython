import numpy as np  
import sys 
import io 
import opcode
import uuid 
import csv 
import json 
csvFileName ="algoData1c8f53cc-a5c3-44a4-9073-ad6747b96709.csv" 
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
user_input = "1\n3\n1 2 5\n6 3 4\n2 7 1\n" 
saved_stdin = sys.stdin 
sys.stdin = io.StringIO(user_input) 
sys.settrace(show_trace) 
def newFunction():
    for _ in range(int(input())):
        n = int(input())
        a = []
        for i in range(n):
            a.append(list(map(int,input().split())))
        a = np.array(a)
        # print(a)
        sums = [a.trace()]
        for i in range(1, n):
            sums.append(a[0:n-i, i:n].trace())
            sums.append(a[i:n, 0:n-i].trace())
        print(max(sums))
newFunction() 

sys.settrace(None) 
sys.stdin = saved_stdin 
