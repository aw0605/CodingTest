import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
ans = 0

for i in range(n):
    idx = i
    while stack and stack[-1][1] > arr[i]:
        idx, h = stack.pop()
        ans = max(ans, (i-idx) * h)
    stack.append([idx, arr[i]])
    
while stack:
    i,h = stack.pop()
    ans = max(ans, (n-i) * h)
    
print(ans)