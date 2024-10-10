import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0] * n

for _ in range(m):
    a, b, k = map(int, sys.stdin.readline().split())
    for j in range(a - 1, b): arr[j] = k

for i in range(n):
    print(arr[i], end=" ")
