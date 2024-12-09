import math
import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(0)
    exit()

is_prime = [0,0] + [1] * (n-1)
for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]:
        for j in range(2, n // i + 1): is_prime[i*j] = 0

primes = []
for i in range(2,n+1):
    if is_prime[i]: primes.append(i)

l,r = 0,0
ans = 0
while r <= len(primes):
    temp = sum(primes[l:r])
    if temp == n:
        ans += 1
        r += 1
    elif temp < n: r += 1
    else: l += 1
        
print(ans)