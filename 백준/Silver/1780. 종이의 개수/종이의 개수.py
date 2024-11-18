import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = [0,0,0]

def division(x,y,n):
    num = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != arr[i][j]:
                for a in range(3):
                    for b in range(3):
                        division(x+a*n//3, y+b*n//3, n//3)
                return
    if num == -1: res[0] += 1
    elif num == 0: res[1] += 1
    else: res[2] += 1

division(0,0,n)

print(res[0],res[1],res[2], sep="\n")