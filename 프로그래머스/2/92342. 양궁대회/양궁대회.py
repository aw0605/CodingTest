from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    maxdiff, max_comb = 0, {}
    
    def calcScore(combi):
        s1,s2 = 0,0
        for i in range(1,11):
            if info[10 - i] < combi.count(i): s1 += i
            elif info[10 - i] > 0: s2 += i
        return s1,s2
    
    def calcDiff(diff, cnt):
        nonlocal maxdiff, max_comb
        if diff > maxdiff:
            max_comb = cnt
            maxdiff = diff
            
    for combi in combinations_with_replacement(range(11), n):
        cnt = Counter(combi)
        s1,s2 = calcScore(combi)
        diff = s1 - s2
        calcDiff(diff, cnt)
        
    if maxdiff > 0:
        answer = [0] * 11
        for n in max_comb: answer[10 - n] = max_comb[n]
        return answer
    else: return [-1]