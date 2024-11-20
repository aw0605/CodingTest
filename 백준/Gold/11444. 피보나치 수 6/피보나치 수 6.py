import sys
from collections import defaultdict

n = int(sys.stdin.readline())
MOD = 1000000007

memo = defaultdict(int)
memo[1], memo[2] = 1,1

def fibo(n):
    if n in memo: return memo[n]
    tmp = n // 2
    if n % 2 == 0: memo[n] = (fibo(tmp) * (2 * fibo(tmp - 1) + fibo(tmp)) % MOD) % MOD
    else: memo[n] = ((fibo(tmp + 1) ** 2) + (fibo(tmp) ** 2)) % MOD
    return memo[n]
    
print(fibo(n))