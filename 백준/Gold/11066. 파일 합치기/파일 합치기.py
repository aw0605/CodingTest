import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[1e9]*k for _ in range(k)]
    sub = [0]*(k+1)
    for i in range(1, k+1): sub[i] = arr[i-1] + sub[i-1]
    for i in range(k): dp[i][i] = 0
    for i in range(2, k+1):
        for j in range(k-i+1):
            for l in range(j, j+i-1):
                dp[j][j+i-1] = min(dp[j][j+i-1], dp[j][l]+dp[l+1][j+i-1]+sub[j+i]-sub[j]) 
    
    print(dp[0][k-1])