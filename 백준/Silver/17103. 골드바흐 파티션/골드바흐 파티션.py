import sys
input = sys.stdin.readline

t = int(input())

def isPrime(n):
    arr = [0,0] + [1] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i*i,n+1, i):
                arr[j] = 0
                
    primes = [i for i,v in enumerate(arr) if v]
    return arr, primes

arr = [False]*2 + [True]*999999

arr, primes = isPrime(1000000)

for _ in range(t):
    ans = 0
    n = int(input())
    for v in primes:
        x = n-v
        if x < v: break
        else:
            if arr[x]: ans += 1
    print(ans)