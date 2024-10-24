import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            cur = arr[i] + arr[j] + arr[k]
            if cur > ans and cur <= m: ans = cur
        
print(ans)