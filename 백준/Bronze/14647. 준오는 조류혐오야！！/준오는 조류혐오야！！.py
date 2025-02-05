import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().strip().split() for _ in range(n)]
total = sum(v.count("9") for row in arr for v in row) 

r9, c9 = 0, 0
r9 = max(sum(v.count('9') for v in row) for row in arr)

for j in range(m):
    curC9 = 0
    for i in range(n):
        curC9 += arr[i][j].count("9")
    c9 = max(c9, curC9)

print(total - max(r9, c9))