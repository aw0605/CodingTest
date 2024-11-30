from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n+1):
    graph[i].sort()

visited1 = [0] * (n+1)
visited2 = [0] * (n+1)

def dfs(r):
    visited1[r] = 1
    print(r, end=" ")
    for v in graph[r]:
        if not visited1[v]: dfs(v)
    
def bfs(r):
    q = deque([r])
    visited2[r] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for x in graph[v]:
            if not visited2[x]:
                q.append(x)
                visited2[x] = 1
                
dfs(r)
print()
bfs(r)