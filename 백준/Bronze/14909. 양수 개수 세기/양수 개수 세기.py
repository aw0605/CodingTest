import sys
input = sys.stdin.readline

arr = map(int, input().split())
ans = sum(1 for n in arr if n > 0)

print(ans)
