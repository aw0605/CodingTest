def solution(n):
# 주어진 자연수를 연속된 자연수의 합으로 표현하는 방법의 수는 주어진 수의 홀수인 약수 갯수는 같다.
    answer = 0

    for i in range(1, n+1, 2):
        if n % i == 0 and i % 2 == 1: answer += 1
        
    return answer