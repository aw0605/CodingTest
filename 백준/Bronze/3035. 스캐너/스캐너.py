import sys
input = sys.stdin.readline

r,c,zr,zc = map(int, input().split())

ans = []
for _ in range(r):
    s = input().strip()
    res = ""
    for i in s: res += i * zc
    for i in range(zr): ans.append(res)
        
for row in ans:
    print(row)