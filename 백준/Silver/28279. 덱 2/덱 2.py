from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    ops = input().split()
    if ops[0] == "1": q.appendleft(int(ops[1]))
    elif ops[0] == "2": q.append(int(ops[1]))
    elif ops[0] == "3":
        print(q.popleft() if q else -1)
    elif ops[0] == "4":
        print(q.pop() if q else -1)
    elif ops[0] == "5": print(len(q))
    elif ops[0] == "6":
        print(0 if q else 1)
    elif ops[0] == "7":
        print(q[0] if q else -1)
    elif ops[0] == "8":
        print(q[-1] if q else -1)
