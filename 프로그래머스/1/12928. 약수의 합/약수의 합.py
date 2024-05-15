def solution(n):
    return n + sum(v for v in range(1,n//2+1) if not n % v)