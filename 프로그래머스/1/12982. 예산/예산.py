def solution(d, budget):
    answer = 0
    d.sort()
    
    for amount in d:
        if budget < amount: break
        budget -= amount
        answer += 1
        
    return answer