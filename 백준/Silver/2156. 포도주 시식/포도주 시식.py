import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [0] * n
dp[0] = arr[0]

if n > 1: dp[1] = arr[0] + arr[1]
if n > 2: dp[2] = max(arr[2]+arr[0], arr[2]+arr[1], dp[1])

for i in range(3,n):
    dp[i] = max(dp[i-3]+arr[i]+arr[i-1], dp[i-2]+arr[i], dp[i-1])
    
print(dp[n-1])