from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y, 0)])
    visited[x][y][0] = 1
    while q:
        x, y, cnt = q.popleft()
        if (x, y) == (n-1, m-1): return visited[x][y][cnt]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] and not cnt:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
                if not board[nx][ny] and not visited[nx][ny][cnt]:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append((nx, ny, cnt))
    return -1

print(bfs(0, 0))