import sys
input = sys.stdin.readline

n = int(input())
res = [[0] * 3 for _ in range(3)]
for _ in range(n):
    a,b,c = map(int, input().split())
    res[0][a-1] += a
    res[1][b-1] += b
    res[2][c-1] += c
    
total = [[i,sum(s)] for i,s in enumerate(res)]

maxS = max(map(lambda x:x[1], total))
candidate = list(filter(lambda x: x[1] == maxS, total))
if len(candidate) > 1:
    max3 = max(map(lambda x: res[x[0]][2], candidate))
    candidate = list(filter(lambda x: res[x[0]][2] == max3, candidate))
if len(candidate) > 1:
    max2 = max(map(lambda x: res[x[0]][1], candidate))
    candidate = list(filter(lambda x: res[x[0]][1] == max2, candidate))
if len(candidate) > 1: print(0, maxS)
else: print(candidate[0][0]+1, candidate[0][1])