import sys
input = sys.stdin.readline

grid = [[0]*100 for _ in range(100)]

for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d): grid[i-1][j-1] = 1

print(sum(sum(row) for row in grid))