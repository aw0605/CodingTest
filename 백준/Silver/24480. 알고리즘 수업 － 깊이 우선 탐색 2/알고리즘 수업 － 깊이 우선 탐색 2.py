import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(n+1):
    graph[i].sort(reverse=True)

cnt = [0] * (n+1)
visited = [0] * (n+1)
t = 1

def dfs(graph, visited, r):
    global t
    visited[r] = 1
    cnt[r] = t
    t += 1
    for x in graph[r]:
        if not visited[x]: dfs(graph, visited, x)
            
dfs(graph, visited, r)

print('\n'.join(str(cnt[i]) for i in range(1,n+1)))