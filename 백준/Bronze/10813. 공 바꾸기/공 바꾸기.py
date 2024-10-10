import sys

n,m = map(int, sys.stdin.readline().split())
arr = [i+1 for i in range(n)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
    
for i in range(n):
    print(arr[i], end=" ")

