import sys
input = sys.stdin.readline

n = int(input())

def fibo1(n):
    memo = [0] * (n+1)
    memo[1] = memo[2] = 1
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def fibo2(n):
    return n-2

print(fibo1(n), fibo2(n))