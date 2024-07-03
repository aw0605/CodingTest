def convert(n, k):
    s = ''
    while n:
        s += str(n % k)
        n //= k
    return s[::-1]

def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n % i == 0: return False
        i += 1
    return True

def solution(n, k):
    s = convert(n, k)
    answer = 0
    for num in s.split('0'):
        if not num: continue
        if isprime(int(num)): answer += 1

    return answer