import sys
import io
import opcode  

# Define a function that uses input()
def greet_user():
    name = input("What is your name? ")
    print("Hello, " + name + "!")


def show_trace(frame, event, arg):
    frame.f_trace_opcodes = True
    code = frame.f_code
    offset = frame.f_lasti
    
    print(f"| {event:10} | {str(arg):>4} |", end=' ')
    print(f"{frame.f_lineno:>4} | {frame.f_lasti:>6} |", end=' ')
    print(f"{opcode.opname[code.co_code[offset]]:<18} | {str(frame.f_locals):<35} |")
    return show_trace

def test():
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
    
# Call the function with a simulated input
user_input = '5\n2 1\n3 2\n1 1\n4 1\n5 3' 
# The "\n" simulates the user pressing the Enter key
saved_stdin = sys.stdin  # Save a reference to the original stdin
sys.stdin = io.StringIO(user_input)  # Redirect stdin to a string buffer
sys.settrace(show_trace)
# for _ in range(int(input())):
#         a,b = map(int,input().split())
#         if (a==1 and b==1):
#             print(1)
#         elif (b==1 and a!=1):
#             print(-1)
#         else:
#             for i in range(1,a+1):
#                 if i!=b:
#                     print(i,end = " ")
#             print(b)
test()
sys.settrace(None)
sys.stdin = saved_stdin  # Restore the original stdin

