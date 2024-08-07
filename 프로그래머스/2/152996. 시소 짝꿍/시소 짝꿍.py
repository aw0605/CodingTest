from itertools import combinations
from collections import Counter

def solution(weights):
    answer = 0
    weights = Counter(weights)
    
    for a, b in combinations(weights.keys(), 2):
        if a*2 == b*3 or a*2 == b*4 or a*3 == b*4 or b*2 == a*3 or b*2 == a*4 or b*3 == a*4: answer += weights[a] * weights[b]

    for v in weights.values():
        if v > 1: answer += v * (v-1) / 2

    return answer
