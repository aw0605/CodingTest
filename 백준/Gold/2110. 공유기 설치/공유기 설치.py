import sys
input = sys.stdin.readline

n,c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

s,e = 1, arr[-1] - arr[0]
dist = 0

while s <= e:
    mid = (s+e) // 2
    cur = arr[0]
    count = 1
    for i in range(1, n):
        if arr[i] >= cur + mid:
            count += 1
            cur = arr[i]
    if count >= c : 
        s = mid + 1
        dist = mid
    else: e = mid - 1
    
    
print(dist)