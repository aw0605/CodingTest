import sys
input = sys.stdin.readline

n = int(input())
arr = [[],[],[]]
for _ in range(n):
    a,b,c = list(map(int,input().split()))
    arr[0].append(a)
    arr[1].append(b)
    arr[2].append(c)
    
scores = [0] * n 
for i in range(3):
    for j in range(n):
        cur = arr[i][j]
        if arr[i].count(cur) > 1: continue
        else: scores[j] += cur
            
for s in scores: print(s)