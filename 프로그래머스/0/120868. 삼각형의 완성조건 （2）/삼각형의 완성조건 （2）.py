def solution(sides):
    answer = 0
    maxS = max(sides)
    minS = min(sides)
    for i in range(maxS-minS+1, maxS+minS): answer+=1
    return answer