from collections import deque
import sys
input = sys.stdin.readline

k = int(input())

def bfs(s, g):
    q = deque([s])
    visited[s] = g
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = -1 * visited[x]
                q.append(i)
            elif visited[x] == visited[i]: return 0
    return 1

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for i in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if not visited[i]:
            res = bfs(i, 1)
            if not res: break

    print('YES' if res else 'NO')