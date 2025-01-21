import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    score = 0
    for j in range(3):
        cur = arr[i][j]
        same = 0
        for k in range(n):
            if i == k: continue
            if cur == arr[k][j]: 
                same = 1
                break
        if not same: score += cur
    print(score)