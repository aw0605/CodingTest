from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())

dist = [0] * 100001

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        x = q.popleft()
        if x == k: return dist[k]
        for i in (x+1,x-1,x*2):
            if 0 <= i <= 100000 and not dist[i]:
                dist[i] = dist[x] + 1
                q.append(i)

print(bfs(n))