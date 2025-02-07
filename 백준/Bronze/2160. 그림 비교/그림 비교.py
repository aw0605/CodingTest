import sys
input = sys.stdin.readline

def diff(i, j):
    cnt = 0
    for a in range(5):
        for b in range(7):
            if arr[i][a][b] != arr[j][a][b]: cnt += 1
    return cnt

n = int(input().strip())
arr = [[list(input().strip()) for _ in range(5)] for _ in range(n)]

a, b = 0, 1 
minDiff = 35
for i in range(n):
    for j in range(i + 1, n):
        cur = diff(i, j)
        if minDiff > cur:
            a, b = i, j
            minDiff = cur

print(a + 1, b + 1)