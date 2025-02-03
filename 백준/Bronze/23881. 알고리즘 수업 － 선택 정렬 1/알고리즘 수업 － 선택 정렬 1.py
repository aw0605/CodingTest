import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n-1, -1, -1):
    maxN = max(arr[:i+1])
    maxIdx = arr.index(maxN)
    if arr[i] < maxN:
        cnt += 1
        if cnt == k:
            print(arr[i], maxN)
            exit()
        arr[i], arr[maxIdx] = arr[maxIdx], arr[i]      
        
print(-1)