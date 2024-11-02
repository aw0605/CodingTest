from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
ans = []

for _ in range(n):
    ops = input().split()
    if ops[0] == "push":
        q.append(ops[1])
    elif ops[0] == "pop":
        ans.append(q.popleft() if q else '-1')
    elif ops[0] == "size":
        ans.append(str(len(q)))
    elif ops[0] == "empty":
        ans.append('1' if len(q) == 0 else '0')
    elif ops[0] == "front":
        ans.append(q[0] if q else '-1')
    elif ops[0] == "back":
        ans.append(q[-1] if q else '-1')

sys.stdout.write("\n".join(ans))
            
            