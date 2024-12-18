import math
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n = int(input())

stars = []
for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))
    
p = [i for i in range(n+1)]

def find(x):
    if p[x] != x: p[x] = find(p[x])
    return p[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: p[b] = a
    else: p[a] = b

edges = []
for i in range(n-1):
    for j in range(i+1, n):
        edges.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))

edges.sort()

ans = 0
for e in edges:
    c, x, y = e
    if find(x) != find(y):
        union(x, y)
        ans += c

print(round(ans, 2))