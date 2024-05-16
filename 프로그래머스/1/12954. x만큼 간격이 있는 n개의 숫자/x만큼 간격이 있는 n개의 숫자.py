def solution(x, n):
    return [0] * n if x == 0 else [v for v in range(x, x*n+1 if x > 0 else x*n-1, x)]