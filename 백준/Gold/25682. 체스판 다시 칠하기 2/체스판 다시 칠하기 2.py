import sys
input = sys.stdin.readline

n,m,k= map(int, input().split())

arr = [input().strip() for _ in range(n)]

def check(start):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if ((i + j) % 2 == 0): v = (arr[i][j] != start)
            else: v = (arr[i][j] == start)

            dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + v

    MIN = n * m
    for i in range(1, n-k+2):
        for j in range(1, m-k+2):
            MIN = min(MIN, dp[i+k-1][j+k-1] - dp[i+k-1][j-1] - dp[i-1][j+k-1] + dp[i-1][j-1])

    return MIN

print(min(check('B'), check('W')))