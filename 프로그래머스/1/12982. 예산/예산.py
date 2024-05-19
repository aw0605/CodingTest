def solution(d, budget):
    answer = 0
    for v in sorted(d):
        budget -= v
        if budget < 0: break
        answer += 1
    return answer