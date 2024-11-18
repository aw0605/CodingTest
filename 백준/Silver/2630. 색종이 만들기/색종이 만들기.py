import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = [0,0]

def division(x,y,n):
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                division(x,y,n//2)
                division(x,y+n//2,n//2)
                division(x+n//2,y,n//2)
                division(x+n//2,y+n//2,n//2)
                return
    if color == 0: res[0] += 1
    else: res[1] += 1
        
division(0,0,n)

print(res[0],res[1],sep="\n")