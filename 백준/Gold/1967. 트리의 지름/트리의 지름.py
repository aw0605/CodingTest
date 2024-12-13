from collections import deque
import sys
input = sys.stdin.readline
 
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
 
def bfs(s):
    visited = [-1] * (n + 1)
    visited[s] = 0
    q = deque()
    q.append(s)
    while q:
        cur = q.popleft()
        for nn, nd in graph[cur]:
            if visited[nn] == -1:
                q.append(nn)
                visited[nn] = visited[cur] + nd
    m = max(visited)
    return [visited.index(m), m]
 
print(bfs(bfs(1)[0])[1])