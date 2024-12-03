from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1: q.append((i, j, k))

def bfs():
    while q:
        z,y,x = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and not arr[nz][ny][nx]:
                arr[nz][ny][nx] = arr[z][y][x] + 1
                q.append((nz, ny, nx))

bfs()

day = 0
for box in arr:
    for row in box:
        for tomato in row:
            if tomato == 0:
                print(-1)
                exit()
        day = max(day, max(row))

print(day - 1)