from heapq import heappop, heappush

def solution(book_time):
    answer = 1

    bookings = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])+10) for s, e in book_time]
    bookings.sort()
    
    heap = []
    for s, e in bookings:
        if not heap:
            heappush(heap,e)
            continue
        if heap[0] <= s: heappop(heap)
        else: answer += 1
        heappush(heap,e)
    
    return answer