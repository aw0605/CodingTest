import sys

n, num = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if arr[i] < num: print(arr[i], end=" ")