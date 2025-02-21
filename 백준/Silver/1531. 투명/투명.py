import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dp = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            dp[i-1][j-1] += 1
            
print(sum(1 for row in dp for cell in row if cell > m))