import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n)]

for _ in range(m):
    a, b, k = map(int, sys.stdin.readline().split())
    for j in range(a - 1, b): arr[j].append(k)

for i in range(n):
    if not arr[i]: print("0", end=" ")
    else: print(arr[i][-1], end=" ")
