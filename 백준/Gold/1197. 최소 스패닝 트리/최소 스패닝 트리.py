import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = []
for _ in range(E):
    graph.append(list(map(int, input().split())))

graph.sort(key=lambda x: x[2])

p = [i for i in range(V + 1)]

def find(x):
    if x != p[x]: p[x] = find(p[x])
    return p[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y: p[y] = x

ans = 0
for s, e, c in graph:
    if find(s) != find(e):
        union(s, e)
        ans += c

print(ans)