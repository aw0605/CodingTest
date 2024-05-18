def solution(n, m):
    nm = n * m
    while m != 0:
        n, m = m, n % m
    return [n, nm // n]