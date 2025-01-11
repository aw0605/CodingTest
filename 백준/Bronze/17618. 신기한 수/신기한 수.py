import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for num in range(1,n+1):
    i = [int(k) for k in str(num)]
    j = sum(i)
    if not num % j: ans += 1
        
print(ans)