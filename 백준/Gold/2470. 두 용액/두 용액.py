import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

l,r = 0,n-1
res = abs(arr[l] + arr[r])

ans = [arr[l], arr[r]]

while l < r:
    temp = arr[l] + arr[r]
    if abs(temp) < res:
        res = abs(temp)
        ans = [arr[l], arr[r]]
        if res == 0: break
    if temp < 0: l += 1
    else: r -= 1

print(ans[0], ans[1])