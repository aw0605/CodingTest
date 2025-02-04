import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))
ans = sum(arr[:k])
for i in range(1, n-k+1):
    cur = sum(arr[i:i+k])
    ans = max(ans, cur)
    
print(ans)