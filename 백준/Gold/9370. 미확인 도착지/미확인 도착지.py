import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())
INF = int(1e9)

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dist = [INF] * (n + 1)
    dist[s] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d: continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dist

for _ in range(t):
    n, m, k = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    array = [int(input()) for _ in range(k)]

    first = dijkstra(s)
    g_dijk = dijkstra(g)
    h_dijk = dijkstra(h)

    ans = []

    for b in array:
        if first[g] + g_dijk[h] + h_dijk[b] == first[b] or first[h] + h_dijk[g] + g_dijk[b] == first[b]:
            ans.append(b)

    ans.sort()

    print(*ans)