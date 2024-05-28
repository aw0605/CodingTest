def solution(s):
    x = ""
    count = 0
    answer = 0
    
    for v in s:
        if not count:
            answer += 1
            x = v
        count += 1 if x == v else -1

    return answer