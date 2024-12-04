import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

V,E = map(int, input().split())
k = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dp = [INF] * (V+1)
heap = []

def dijkstra(s):
    dp[s] = 0
    heapq.heappush(heap,(0, s))

    while heap:
        curW, cur = heapq.heappop(heap)
        if dp[cur] < curW: continue
        for w, nextN in graph[cur]:
            nextW = w + curW
            if nextW < dp[nextN]:
                dp[nextN] = nextW
                heapq.heappush(heap,(nextW, nextN))

dijkstra(k)

for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])