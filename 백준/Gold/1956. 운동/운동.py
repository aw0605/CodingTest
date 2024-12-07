import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
graph = [[INF] * (V+1) for _ in range(V+1)]
for _ in range(E):
    x, y, c = map(int, input().split())
    graph[x][y] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

ans = INF

for i in range(1, V+1):
    ans = min(ans, graph[i][i])

print(-1 if ans == INF else ans)