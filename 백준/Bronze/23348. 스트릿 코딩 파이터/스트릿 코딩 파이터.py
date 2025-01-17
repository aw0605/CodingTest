import sys
input = sys.stdin.readline

s = list(map(int, input().split()))

n = int(input())
ans = 0
for i in range(n):
    res = 0
    for _ in range(3):
        a,b,c = map(int, input().split())
        res += a * s[0] + b * s[1] + c * s[2]
    ans = max(ans, res)
    
print(ans)