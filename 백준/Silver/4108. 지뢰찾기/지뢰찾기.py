import sys
input = sys.stdin.readline

direct = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (1, -1), (-1, 1), (-1, -1)]

while True:
    r,c = map(int, input().split())
    if r == 0 and c == 0: break
    arr = [list(input().strip()) for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if arr[i][j] == "*": continue
            cnt = 0
            for x,y in direct:
                dx, dy = i+x, j+y
                if dx < 0 or dx >= r or dy < 0 or dy >= c: continue
                if arr[dx][dy] == "*": cnt += 1
            arr[i][j] = str(cnt)
            
    for row in arr: print("".join(row))