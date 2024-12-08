import sys
input = sys.stdin.readline
INF = sys.maxsize

n, s = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
temp = 0

ans = INF

while True:
    if temp >= s:
        ans = min(ans, r - l)
        temp -= arr[l]
        l += 1
    elif r == n: break
    else:
        temp += arr[r]
        r += 1

print(0 if ans == INF else ans)