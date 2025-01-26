import sys
input = sys.stdin.readline

r,c,zr,zc = map(int, input().split())
arr = [input().strip() for _ in range(r)]
for i in range(r):
    ans = ""
    for j in range(c): ans += arr[i][j] * zc
    for j in range(zr): print(ans)