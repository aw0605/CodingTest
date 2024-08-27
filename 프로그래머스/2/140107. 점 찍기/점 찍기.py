import math

def solution(k, d):
    answer = 0
    
    def maxY(x):
        return math.floor(math.sqrt(d * d - x * x))
    
    for x in range(0, d + 1, k):
        answer += (math.floor(maxY(x) / k) + 1)
    
    return answer