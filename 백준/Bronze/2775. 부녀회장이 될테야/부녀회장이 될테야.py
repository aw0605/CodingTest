import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k, n = int(input()), int(input())
    li = [i for i in range(1, n + 1)]
    for _ in range(k):
        li = [sum(li[:j+1]) for j in range(n)]
    print(li[-1])