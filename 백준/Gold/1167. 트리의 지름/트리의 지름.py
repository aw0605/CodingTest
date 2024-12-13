import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
 
v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    nodes = list(map(int, input().split()))
    for n in range(1, len(nodes)-2, 2):
        graph[nodes[0]].append((nodes[n], nodes[n + 1]))
 
def dfs(s, d):
    for nn, nd in graph[s]:
        if visited[nn] == -1:
            visited[nn] = d + nd
            dfs(nn, d + nd)

visited = [-1] * (v + 1)
visited[1] = 0
dfs(1, 0)
 
last = visited.index(max(visited))
visited = [-1] * (v + 1)
visited[last] = 0
dfs(last, 0)
 
print(max(visited))