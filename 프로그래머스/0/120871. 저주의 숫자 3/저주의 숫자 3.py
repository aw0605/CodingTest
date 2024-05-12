def solution(n):
    answer = 1
    for i in range(1,n):
        answer += 1
        while "3" in str(answer) or answer % 3 == 0: answer += 1
    return answer