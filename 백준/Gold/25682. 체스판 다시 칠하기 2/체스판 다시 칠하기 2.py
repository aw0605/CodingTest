import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
dp = [[0]*(M+1) for _ in range(N+1)]

check = 'BW'
for i in range(1, N+1):
    line = input().rstrip()
    for j, v in enumerate(line, 1):
        dp[i][j] = int(v != check[(i+j)%2]) + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

answer = K*K
for i in range(K, N+1):
    for j in range(K, M+1):
        tmp = dp[i][j] - dp[i-K][j] - dp[i][j-K] + dp[i-K][j-K]
        answer = min(answer, tmp, K*K-tmp)

print(answer)