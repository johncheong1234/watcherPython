import opcode  
import sys
import csv
from functions import *

# def fib(n):
#     i, f1, f2 = 1, 1, 1
#     while i < n:
#         f1, f2 = f2, f1 + f2
#         i += 1
#     return f1

def firstMissingPositive(nums):
    # res = 1
    for i in range(len(nums)):
        while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
            tmp = nums[i]-1
            nums[i], nums[tmp] = nums[tmp], nums[i]
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    
    return len(nums)+1

# create recursive function with base case
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# create a list called algoData
algoData = []

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


print(header)
sys.settrace(show_trace)
isMatch("aa", "a*")
sys.settrace(None)

