def solution(n):
    answer = 1
    factorial = 1
    while factorial <= n:
        answer += 1
        factorial = factorial * answer
    return answer - 1