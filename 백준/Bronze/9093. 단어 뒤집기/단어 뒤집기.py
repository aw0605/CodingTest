import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    S = list(input().split())
    for s in S:
        print(s[::-1],end=" ")