import sys
input = sys.stdin.readline

n = int(input())
cur = int(input())
arr = [int(input()) for _ in range(n-1)]
arr.sort(reverse = True)

if n == 1:
    print(0)
    exit()
    
ans = 0
while arr[0] >= cur:
    arr[0] -= 1
    cur += 1
    ans += 1
    arr.sort(reverse = True)

print(ans)