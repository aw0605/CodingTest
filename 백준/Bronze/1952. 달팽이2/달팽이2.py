m, n = map(int, input().split())

visited = [[0] * n for _ in range(m)]
visited[0][0] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
d = 0
total = 1
ans = 0

while total < m * n:
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
        x, y = nx, ny
        visited[x][y] = 1
        total += 1
    else:
        d = (d + 1) % 4
        ans += 1

print(ans)