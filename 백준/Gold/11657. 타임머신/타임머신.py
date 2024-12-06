import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
    
dist = [INF] * (n + 1)

def bellmanFord(s):
    dist[s] = 0
    for i in range(1, n + 1):
        for j in range(m):
            cur, next, t = graph[j][0], graph[j][1], graph[j][2]
            if dist[cur] != INF and dist[next] > dist[cur] + t:
                dist[next] = dist[cur] + t
                if i == n: return 1
    return 0

res = bellmanFord(1)

if res: print(-1)
else:
    for i in range(2, n + 1):
        print(-1 if dist[i] == INF else dist[i])