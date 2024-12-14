import sys
input = sys.stdin.readline

def dfs(s):
    for nn in graph[s]:
        if parent[s] == nn: continue
        if visited[nn]: return True
        parent[nn] = s
        visited[nn] = 1
        if dfs(nn): return True
    return False

case = 0
while True:
    case += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
        
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)      
        
    visited = [0] * (n+1)
    parent = [-1] * (n+1)
    count = 0

    for node in range(1, n+1):
        if not visited[node]:
            parent[node] = node
            visited[node] = 1
            if not dfs(node): count += 1
    
    if count == 0: print(f'Case {case}: No trees.')
    elif count == 1: print(f'Case {case}: There is one tree.')
    else: print(f'Case {case}: A forest of {count} trees.')