def solution(n, stations, w):
    answer = 0
    cur = 1
    i = 0
    
    while cur <= n:
        if i < len(stations) and cur >= stations[i] - w:
            cur = stations[i] + w + 1
            i += 1
        else:
            cur += 2 * w + 1
            answer += 1

    return answer