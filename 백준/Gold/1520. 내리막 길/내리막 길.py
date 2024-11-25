import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]
dx, dy = [1,-1,0,0], [0,0,1,-1]

def dfs(x, y):
    if x == m-1 and y == n-1: return 1
    if dp[x][y] != -1: return dp[x][y]
    
    ways = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and arr[x][y] > arr[nx][ny]:
            ways += dfs(nx, ny)
            
    dp[x][y] = ways
    return dp[x][y]

print(dfs(0,0))