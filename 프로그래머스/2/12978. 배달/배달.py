import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    dist = [float("inf")] * (N+1)
    dist[1] = 0
    
    for a,b,cost in road:
        graph[a].append((b,cost))
        graph[b].append((a,cost))
        
    heap = []
    heapq.heappush(heap, (0,1))
    while heap: 
        d,n = heapq.heappop(heap)
        for next_n, next_d in graph[n]:
            cost = d + next_d
            if cost < dist[next_n]:
                dist[next_n] = cost
                heapq.heappush(heap, (cost, next_n))
    
    return sum(1 for d in dist if d <= K)