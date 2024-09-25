from collections import deque

def solution(maps):
    move = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    n,m = len(maps),len(maps[0])
    dist = [[-1] * m for _ in range(n)]

    def bfs(s):
        q = deque([s])
        dist[s[0]][s[1]] = 1
        while q:
            cur = q.popleft()
            for direct in move:
                r, c = cur[0] + direct[0], cur[1] + direct[1]
                if r < 0 or r >= n or c < 0 or c >= m: continue
                if maps[r][c] == 0: continue
                if dist[r][c] == -1:
                    q.append([r, c])
                    dist[r][c] = dist[cur[0]][cur[1]] + 1
        return dist

    bfs([0, 0])
    return dist[n - 1][m - 1]