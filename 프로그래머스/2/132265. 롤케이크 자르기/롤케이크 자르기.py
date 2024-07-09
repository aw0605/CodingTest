from collections import Counter

def solution(topping):
    answer = 0
    brother = Counter(topping)
    chulsu = set()
    
    for v in topping:
        brother[v] -= 1
        if brother[v] == 0: del brother[v]
        chulsu.add(v)
        if len(brother) == len(chulsu): answer += 1
        
    return answer