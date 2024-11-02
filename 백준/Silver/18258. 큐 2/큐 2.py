from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    ops = input().split()
    if ops[0] == "push": q.append(int(ops[1]))
    elif ops[0] == "pop":
        if q: print(q.popleft())
        else: print(-1)
    elif ops[0] == "size": print(len(q))
    elif ops[0] == "empty":
        if not q: print(1)
        else: print(0)
    elif ops[0] == "front":
        if not q: print(-1)
        else: print(q[0])
    elif ops[0] == "back":
        if not q: print(-1)
        else: print(q[-1])