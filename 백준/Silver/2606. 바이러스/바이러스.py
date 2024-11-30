import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [0] * (n+1)

def dfs(s):
    visited[s] = 1
    for v in graph[s]:
        if not visited[v]: dfs(v)

dfs(1)
print(sum(visited) - 1)   