import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
for i in range(1,n+1):
    print(len(arr[i]))