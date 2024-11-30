import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx,dy = [0, 0, 1, -1],[1, -1, 0, 0]
res = []
cnt = 0

def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n: return
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            res.append(cnt)
            cnt = 0

res.sort()

print(len(res))
print(*res)