from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    que = deque()
    que.append((1, 0, 0))

    maps[0][0] = 0

    while que:
        count, i, j = que.popleft()
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if y == n - 1 and x == m - 1: return count + 1
            if 0 <= y < n and 0 <= x < m and maps[y][x]:
                que.append((count + 1, y, x))
                maps[y][x] = 0

    return -1