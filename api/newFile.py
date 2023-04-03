import sys 
import io 
import opcode
def show_trace(frame, event, arg):
    frame.f_trace_opcodes = True
    code = frame.f_code
    offset = frame.f_lasti
    print(f"| {event:10} | {str(arg):>4} |", end=' ')
    print(f"{frame.f_lineno:>4} | {frame.f_lasti:>6} |", end=' ')
    print(f"{opcode.opname[code.co_code[offset]]:<18} | {str(frame.f_locals):<35} |")
    return show_trace
user_input = "2\n3 2\n5 3\n" 
saved_stdin = sys.stdin 
sys.stdin = io.StringIO(user_input) 
sys.settrace(show_trace) 
def newFunction():
    for _ in range(int(input())):
        a,b = map(int,input().split())
        if (a==1 and b==1):
            print(1)
        elif (b==1 and a!=1):
            print(-1)
        else:
             for i in range(1,a+1):
                 if i!=b:
                     print(i,end = " ")
             print(b)
newFunction() 

sys.settrace(None) 
sys.stdin = saved_stdin 
