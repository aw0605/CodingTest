def solution(arr, divisor):
    answer = sorted(v for v in arr if not v % divisor)
    return answer if len(answer) else [-1]