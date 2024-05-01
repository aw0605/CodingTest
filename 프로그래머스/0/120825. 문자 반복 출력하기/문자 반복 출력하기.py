def solution(my_string, n):
    answer = ''
    for v in my_string:
        answer += v * n
    return answer