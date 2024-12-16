import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
p = [i for i in range(n)]

def find(v):
    if v != p[v]: p[v] = find(p[v])
    return p[v]

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y: p[y] = x
    else: p[x] = y
        
for i in range(n):
    link = list(map(int,input().split()))
    for j in range(n):
        if link[j]: union(i,j)
    
p = [-1] + p
path = list(map(int,input().split()))
s = p[path[0]]

for i in range(1,m):
    if p[path[i]] != s:
        print("NO")
        break
else: print("YES")