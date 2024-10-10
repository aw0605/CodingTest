import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

a,b = min(arr), max(arr)

print(a,b)