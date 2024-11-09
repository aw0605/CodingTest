import sys

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]

def check(y, x, num):
    for i in range(9): # 가로, 세로 체크
        if arr[y][i] == num or arr[i][x] == num: return False
    
    for i in range(3): # 3x3영역 체크
        for j in range(3):
            if arr[y // 3 * 3 + i][x // 3 * 3 + j] == num: return False
    return True

def dfs(n):
    if n == len(blank):
        for row in arr: 
            print(*row) 
        exit() 
    
    for num in range(1,10):
        y, x = blank[n]
        if check(y, x, num):
            arr[y][x] = num
            dfs(n+1)
            arr[y][x] = 0
            
dfs(0)