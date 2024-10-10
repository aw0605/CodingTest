import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
num = int(sys.stdin.readline())
ans = 0

for i in range(n):
    if arr[i] == num: ans += 1

print(ans)