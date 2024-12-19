import sys
input = sys.stdin.readline

n,m = map(int, input().split())
p = list(range(n+1))

edges = [0] * (n+1)
for i in range(1, n+1):
    edges[i] = list(map(int, input().split()))

def find(v):
    if v != p[v]:p[v] = find(p[v])
    return p[v]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: p[b] = a
    else: p[a] = b
        
def dist(xy1, xy2):
    x1, y1 = xy1
    x2, y2 = xy2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

possible = []
for i in range(1, len(edges)-1):
    for j in range(i+1, len(edges)):
        possible.append([dist(edges[i], edges[j]), i, j])

possible.sort()

ans = 0
for v in possible:
    c, x, y = v
    if find(x) != find(y):
        union(x, y)
        ans += c

print(f'{ans:.2f}')