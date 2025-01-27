import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m,n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    ans = 0
    for i in range(n):
        b = m-1
        for j in range(m-1,-1,-1):
            if arr[j][i]:
                ans += b-j
                b -= 1
    print(ans)