def gcd(n, m):
    while m: n, m = m, n % m
    return n

def lcm(n, m):
    return n * m // gcd(n, m)

def solution(arr):
    answer = 1
    for v in arr:
        answer = lcm(answer, v)
    return answer