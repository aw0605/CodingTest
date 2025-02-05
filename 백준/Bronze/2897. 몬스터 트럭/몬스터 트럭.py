import sys
input = sys.stdin.readline

r,c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

ans = [0] * 5
for i in range(r-1):
    for j in range(c-1):
        check = [
            arr[i][j], arr[i][j + 1],
            arr[i + 1][j], arr[i + 1][j + 1]
        ]
        if "#" in check: continue
        xCnt = check.count("X")
        ans[xCnt] += 1

for v in ans: print(v)