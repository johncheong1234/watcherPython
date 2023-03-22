import opcode  
import sys

# def fib(n):
#     i, f1, f2 = 1, 1, 1
#     while i < n:
#         f1, f2 = f2, f1 + f2
#         i += 1
#     return f1

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
    # res = len(nums)+1


def show_trace(frame, event, arg):
    frame.f_trace_opcodes = True
    code = frame.f_code
    offset = frame.f_lasti
    
    if event == 'line':
        print(f"| {event:10} | {str(arg):>4} |", end=' ')
        print(f"{frame.f_lineno:>4} | {frame.f_lasti:>6} |", end=' ')
        print(f"{opcode.opname[code.co_code[offset]]:<18} | {str(frame.f_locals):<35} |")
    return show_trace

header = f"| {'event':10} | {'arg':>4} | line | offset | {'opcode':^18} | {'locals':^35} |"
print(header)
sys.settrace(show_trace)
# isMatch("aa", "a*")
firstMissingPositive([0,1,2])
sys.settrace(None)