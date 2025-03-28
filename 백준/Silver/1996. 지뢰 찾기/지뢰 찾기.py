import sys
input = sys.stdin.readline

direct = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

n = int(input())
arr = [list(input().strip()) for _ in range(n)]

ans = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] != ".": ans[i][j] = "*"
        else:
            cnt = 0
            for k in direct:
                if 0 <= (i+k[0]) <= n-1 and 0 <= (j+k[1]) <= n-1 and arr[i+k[0]][j+k[1]] != ".": 
                    cnt += int(arr[i+k[0]][j+k[1]])
            if cnt > 9: cnt = "M"
            ans[i][j] = str(cnt)
            
for row in ans:
    print(*row, sep="")