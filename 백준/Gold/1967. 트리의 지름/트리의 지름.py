import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
 
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
 
def dfs(s, d):
    for nn, nd in graph[s]:
        if visited[nn] == -1:
            visited[nn] = d + nd
            dfs(nn, d + nd)

visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)

last = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[last] = 0
dfs(last, 0)

print(max(visited))