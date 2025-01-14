import sys
input = sys.stdin.readline

n, x, k = map(int, input().split())

ans = x
for _ in range(k):
    a, b = map(int, input().split())
    if ans == a: ans = b
    elif ans == b: ans = a

print(ans)