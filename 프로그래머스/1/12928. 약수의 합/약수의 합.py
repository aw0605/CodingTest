def solution(n):
    return sum(v for v in range(1,n+1) if not n % v)