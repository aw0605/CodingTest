def solution(priorities, location):
    queue =  [[i,v] for i,v in enumerate(priorities)]
    
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < v[1] for v in queue): queue.append(cur)
        else:
            answer += 1
            if cur[0] == location: return answer