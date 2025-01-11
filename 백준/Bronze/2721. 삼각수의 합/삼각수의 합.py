import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ans = sum(k*sum(range(k+2)) for k in range(1, n+1))
    print(ans)