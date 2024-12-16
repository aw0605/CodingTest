import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split())
p = [i for i in range(0,n+1)]

def find_p(v):
    if p[v] != v: p[v] = find_p(p[v])
    return p[v]

def union_p(a,b):
    a = find_p(a)
    b = find_p(b)
    if a < b: p[b] = a
    else: p[a] = b

for _ in range(m):
    c, a, b = map(int, input().split())
    if not c: union_p(a,b)
    else:
        if find_p(a) == find_p(b): print("YES")
        else: print("NO")