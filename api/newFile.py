import sys 
import io 
user_input = "4\n1 1\n3 2\n4 1\n5 3\n" 
saved_stdin = sys.stdin 
sys.stdin = io.StringIO(user_input) 
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
sys.stdin = saved_stdin 
