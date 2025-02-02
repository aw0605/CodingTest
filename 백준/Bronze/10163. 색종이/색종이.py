import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for x in range(1,n+1):
    sx,sy, w,h = map(int, input().split())
    for y in range(sy,sy+h):
        arr[y][sx:sx+w] = [x] * w
        
for x in range(1,n+1):
    res = 0
    for y in range(1001):
        res += arr[y].count(x)
    print(res)