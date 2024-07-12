import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville: heapq.heappush(heap, i)

    while heap[0] < K:
        if len(heap) == 1 and heap[0] < K: return -1
    
        smallest = heapq.heappop(heap)
        heapq.heappush(heap, smallest + heapq.heappop(heap) * 2)
        answer += 1
    
    return answer