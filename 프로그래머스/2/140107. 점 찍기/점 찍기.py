def solution(k, d):
    answer = 0
    for y in range(0, d, k):
        x = (d**2 - y**2)**0.5
        answer += x//k
    return answer + d//k + 1