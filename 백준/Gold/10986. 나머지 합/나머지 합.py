import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

sum_p = [0] * (n+1)
count = [0] * (m+1)

for i in range(n):
    sum_p[i+1] = (sum_p[i] + arr[i]) % m
    count[sum_p[i+1]] += 1
    
ans = count[0]

for i in range(m+1):
    ans += (count[i] * (count[i]-1)) // 2
    
print(ans)