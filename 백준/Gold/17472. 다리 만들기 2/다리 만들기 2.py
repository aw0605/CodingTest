from collections import deque
import heapq
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
move = [(0,1),(1,0),(0,-1),(-1,0)]
land = dict()
arr = []

landNum = 0
for i in range(n):
    for j in range(m):
        if board[i][j] and not visited[i][j]:
            q = deque([(i,j)])
            visited[i][j] = 1
            land[(i,j)] = landNum
            arr.append((i,j,landNum))
            while q:
                x,y = q.popleft()
                for a,b in move:
                    dx, dy = x+a, y+b
                    if 0<=dx<n and 0<=dy<m and not visited[dx][dy] and board[dx][dy]:
                        q.append((dx,dy))
                        visited[dx][dy] = 1
                        land[(dx,dy)] = landNum
                        arr.append((dx,dy,landNum))
            landNum += 1

edges = []
for x,y,cur in arr:
    for a,b in move:
        dist = 0
        dx, dy = x+a, y+b
        while True:
            if 0<=dx<n and 0<=dy<m:
                to = land.get((dx,dy))
                if cur == to: break
                if to == None:
                    dx += a
                    dy += b
                    dist += 1
                    continue
                if dist < 2: break
                edges.append((dist,cur,to))
                break
            else: break
edges.sort(reverse=True)

def find(v):
    if v != p[v]: p[v] = find(p[v])
    return p[v]

def union(x,y):
    x = find(x)
    y = find(y)
    p[y] = x

ans = 0
cnt = landNum-1
p = [i for i in range(landNum)]
while cnt:
    try: c,a,b = edges.pop()
    except:
        print(-1)
        sys.exit()
        
    if find(a) != find(b):
        union(a,b)
        ans += c
        cnt -= 1
        
print(ans)