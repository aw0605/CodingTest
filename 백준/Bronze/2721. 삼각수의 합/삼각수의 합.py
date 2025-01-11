import sys
input = sys.stdin.readline

def T(n):
    ans = 0
    for i in range(1,n+1): ans += i
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for k in range(1,n+1):
        ans += k * T(k+1)
    print(ans)