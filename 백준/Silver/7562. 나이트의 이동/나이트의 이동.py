from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

dx,dy = [-2, -1, 1, 2, 2, 1, -1, -2],[1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    q = deque()
    q.append([sx,sy])
    visited[sx][sy] = 1
    while q:
        cx,cy = q.popleft()
        if cx == ex and cy == ey: return visited[cx][cy]-1
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < l and 0<= ny < l and not visited[nx][ny]:
                q.append([nx,ny])
                visited[nx][ny] = visited[cx][cy] + 1

for _ in range(t):
    l = int(input())
    sx,sy = map(int, input().split())
    ex,ey = map(int, input().split())
    
    visited = [[0] * l for _ in range(l)]
    
    print(0) if sx == ex and sy == ey else print(bfs())