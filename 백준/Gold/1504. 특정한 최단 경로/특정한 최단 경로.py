import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

s1, s2 = map(int, input().split())

def dijkstra(s, e):
    dist = [INF] * (N+1)
    dist[s] = 0
    heap = [(0, s)]
    while heap:
        curD, curN = heapq.heappop(heap)
        if curD > dist[curN]:
            continue
        for l, nextN in graph[curN]:
            distance = curD + l
            if distance < dist[nextN]:
                dist[nextN] = distance
                heapq.heappush(heap, (distance, nextN))
    return dist[e]

p1 = dijkstra(1, s1) + dijkstra(s1, s2) + dijkstra(s2, N)
p2 = dijkstra(1, s2) + dijkstra(s2, s1) + dijkstra(s1, N)

print(-1 if p1 >= INF and p2 >= INF else min(p1,p2))