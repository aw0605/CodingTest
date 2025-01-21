import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [input().split() for _ in range(n)]
    arr.sort(key=lambda x: int(x[1]))
    print(arr[-1][0])