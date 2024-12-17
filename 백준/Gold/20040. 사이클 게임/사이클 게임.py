import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
p = [i for i in range(n)]

ans = 0

def find(v):
    if p[v] != v: p[v] = find(p[v])
    return p[v]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: p[b] = a
    else: p[a] = b

for i in range(1,m+1):
    a,b = map(int, input().split())
    if find(a) == find(b):
        ans = i
        break
    union(a,b)
    
print(ans)