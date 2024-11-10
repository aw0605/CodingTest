import sys
input = sys.stdin.readline

n = int(input())

cnt1, cnt2 = 0, 0

def fibo1(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else: return fibo1(n-1) + fibo1(n-2)

memo = [0] * (n+1)
def fibo2(n):
    memo[1] = memo[2] = 1
    global cnt2
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
        cnt2 += 1
    return memo[n]

fibo1(n)
fibo2(n)

print(cnt1, cnt2)