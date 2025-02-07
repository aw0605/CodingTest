import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n-1,0,-1):
    maxIdx = arr.index(max(arr[:i+1]))
    if i != maxIdx:
        arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
        cnt += 1
        if cnt == k: 
            print(*arr)
            exit()
            
print(-1)