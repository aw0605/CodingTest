import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    x, y = int("".join(list(input().split()))), int("".join(list(input().split())))
    arr = list(map(int, input().split()))
    arr += arr[:m]
    
    ans = 0
    for i in range(n):
        res = int("".join(map(str, arr[i:i+m])))
        if x <= res <= y: ans += 1
    print(ans)