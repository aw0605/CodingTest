import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] != ".":
            arr[i][m-j-1] = arr[i][j]
            
for row in arr:
    print("".join(row))