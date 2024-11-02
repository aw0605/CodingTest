import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack =[]

turn = 1
for v in arr:
    stack.append(v)
    while stack and stack[-1] == turn:
        stack.pop()
        turn += 1
        
print("Sad" if stack else "Nice")