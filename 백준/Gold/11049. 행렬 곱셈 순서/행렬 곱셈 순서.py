import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = [a for a, _ in arr] + [arr[-1][1]]

dp = [[0]*n for _ in range(n)]

for i in range(1,n):
    for j in range(n-i):
        e = j + i
        mul = arr[j] * arr[e+1]
        minimum =  min(x + y + z * mul for x, y, z in zip(dp[j][j:e], dp[e][j+1:e+1], arr[j+1:e+1]))
        dp[j][e] = dp[e][j] = minimum

print(dp[0][-1])