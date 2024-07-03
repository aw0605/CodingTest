def isPrime(n):
    if n <= 1: return False
    if n == 2: return True
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0: return False
    return True

def solution(n, k):
    num = "";
    while n:
        num += str(n % k)
        n //= k
    
    arr = num[::-1].split("0")
        
    return len([v for v in arr if v and isPrime(int(v))])