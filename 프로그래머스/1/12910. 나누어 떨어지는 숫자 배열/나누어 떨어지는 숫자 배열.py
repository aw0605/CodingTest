def solution(arr, divisor):
    return sorted(v for v in arr if not v % divisor) or [-1]