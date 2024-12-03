from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

ladders = defaultdict() 
for _ in range(n):
    x,y = map(int, input().split())
    ladders[x] = y

snakes = defaultdict() 
for _ in range(m):
    x,y = map(int, input().split())
    snakes[x] = y
    
board = [0] * 101

def bfs(s):
    q = deque()
    q.append(s)
    board[s] = 1
    while q:
        cur = q.popleft()
        for i in range(1,7):
            nextC = cur + i
            if 0 < nextC <= 100:
                if nextC in ladders: nextC = ladders[nextC]
                if nextC in snakes: nextC = snakes[nextC]
                if not board[nextC]:
                    board[nextC] = board[cur] + 1
                    q.append(nextC)
                    
bfs(1)
print(board[100] - 1)