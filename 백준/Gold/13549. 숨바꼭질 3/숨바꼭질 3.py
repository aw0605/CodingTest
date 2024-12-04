from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
visited = [0] * 100001

def bfs(s,b):
    q = deque([s])
    visited[s] = 1
    while q:
        x = q.popleft()
        if x == b: return visited[x] - 1
        for nx in (2*x, x-1, x+1):
            if 0 <= nx <= 100000 and not visited[nx]:
                if nx == 2 * x: visited[nx] = visited[x]
                else: visited[nx] = visited[x] + 1
                q.append(nx)
                 
print(bfs(n,k))