from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        p = queue.popleft()
        s = 0
        for q in queue:
            s += 1
            if p > q: break 
        answer.append(s)
        
    return answer