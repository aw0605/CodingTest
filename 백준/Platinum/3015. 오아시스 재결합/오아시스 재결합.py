import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
ans = 0

for cur in arr:
  while stack and stack[-1][0] < cur: ans += stack.pop()[1]

  if not stack:
    stack.append((cur, 1))
    continue

  if stack[-1][0] == cur:
    cnt = stack.pop()[1]
    ans += cnt
    if stack: ans += 1
    stack.append((cur, cnt+1))
  else:
    stack.append((cur, 1))
    ans += 1

print(ans)