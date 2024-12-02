from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

day = 0

q = deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1: q.append([i,j])

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx,ny])

bfs()

for row in arr:
    for tomato in row:
        if not tomato:
            print(-1)
            exit()
    day = max(day, max(row))
    
print(day - 1)