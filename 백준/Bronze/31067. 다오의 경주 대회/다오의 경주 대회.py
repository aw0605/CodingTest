import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1,n):
    if arr[i-1] >= arr[i]:
        arr[i] += k
        cnt += 1
        if arr[i-1] >= arr[i]:
            print(-1)
            exit()
        
print(cnt)