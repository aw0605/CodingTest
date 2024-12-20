import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n,r,q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (n+1)

def dfs(cur):
    visited[cur] = 1
    for i in graph[cur]:
        if not visited[i]:
            visited[cur] += dfs(i)
    return visited[cur]

dfs(r)

for _ in range(q):
    v = int(input())
    print(visited[v])