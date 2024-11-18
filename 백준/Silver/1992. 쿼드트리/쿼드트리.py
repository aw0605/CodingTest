import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]

ans = ""

def division(x,y,n):
    global ans
    num = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if num != arr[i][j]:
                ans += "("
                division(x,y,n//2)
                division(x,y+n//2,n//2)
                division(x+n//2,y,n//2)
                division(x+n//2,y+n//2,n//2)
                ans += ")"
                return
    ans += num
        
division(0,0,n)

print(ans)