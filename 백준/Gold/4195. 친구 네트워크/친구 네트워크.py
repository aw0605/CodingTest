import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

t = int(input().strip())

def find(v):
    if p[v] != v: p[v] = find(p[v])
    return p[v]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        p[b] = a
        num[a] += num[b]
    print(num[a])

for _ in range(t):
    f = int(input())
    p, num = {}, {}
    for _ in range(f):
        a, b = input().strip().split()
        if a not in p:
            p[a] = a
            num[a] = 1
        if b not in p:
            p[b] = b
            num[b] = 1
        union(a, b)