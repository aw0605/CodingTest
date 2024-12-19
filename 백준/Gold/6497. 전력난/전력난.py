import sys
input = sys.stdin.readline

def find(v):
    if p[v] != v: p[v] = find(p[v])
    return p[v]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b: p[b] = a
    else: p[a] = b

while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0: break

    p = [i for i in range(n)]
    graph = []
    for _ in range(m):
        a,b,c = map(int, input().split())
        graph.append((a,b,c))
        
    graph.sort(key=lambda x: x[2])
    
    ans = 0
    for a,b,c in graph:
        if find(a) != find(b): union(a,b)
        else: ans += c 
            
    print(ans)