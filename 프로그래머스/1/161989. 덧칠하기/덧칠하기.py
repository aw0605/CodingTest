def solution(n, m, section):
    answer = 0
    paint = 0
    for v in section:
        if paint < v: 
            answer += 1
            paint = v + m - 1
    return answer