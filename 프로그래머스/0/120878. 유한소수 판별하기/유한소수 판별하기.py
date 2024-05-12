from math import gcd

def solution(a, b):
    b = b / gcd(a, b)
    for i in [2, 5]:
        while b % i == 0: b //= i

    return 1 if b == 1 else 2