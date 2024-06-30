def solution(priorities, location):
    total = len(priorities)
    answer = 0
    cur = 0
    while True:
        if max(priorities) == priorities[cur % total]:
            priorities[cur % total] = 0
            answer += 1
            if cur % total == location: break
        cur += 1
        
    return answer