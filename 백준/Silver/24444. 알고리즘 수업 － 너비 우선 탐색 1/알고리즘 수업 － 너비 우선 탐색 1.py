from collections import deque
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
    graph[i].sort()
    
visited = [0] * (n+1)
t = 1

def bfs(graph, visited, r):
    global t
    q = deque([r])
    visited[r] = t
    while q:
        v = q.popleft()
        for x in graph[v]:
            if visited[x] == 0:
                t += 1
                visited[x] = t
                q.append(x)
                
bfs(graph, visited, r)

print("\n".join(str(visited[i]) for i in range(1,n+1)))