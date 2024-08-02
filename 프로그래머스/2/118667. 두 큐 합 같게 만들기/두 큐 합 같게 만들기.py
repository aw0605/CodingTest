def solution(queue1, queue2):
    target = (sum(queue1) + sum(queue2)) // 2
    sum1 = sum(queue1)
    queue3 = queue1 + queue2 + queue1
    s = 0
    e = len(queue1) - 1
    answer = 0
    
    while True:
        if sum1 == target: return answer
        if sum1 < target:
            e += 1
            if e >= len(queue3): return -1
            sum1 += queue3[e]
        else:
            sum1 -= queue3[s]
            s += 1
        answer += 1