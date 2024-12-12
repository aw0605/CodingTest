from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
s, e = map(int, input().split())

dist = [INF] * (n+1)
prev = [0] * (n+1)

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        w, node = heapq.heappop(q)
        if dist[node] < w: continue
        for an, aw in graph[node]:
            cost = w + aw
            if cost < dist[an]:
                dist[an] = cost
                prev[an] = node
                heapq.heappush(q, (cost, an))

dijkstra(s)

path = [e]
cur = e
while cur != s:
    cur = prev[cur]
    path.append(cur)

path.reverse()

print(dist[e])
print(len(path))
print(' '.join(map(str, path)))