import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

s,e = 1, k

while s <= e:
    mid = (s+e) // 2
    count = 0
    for i in range(1, n+1): count += min(n, mid//i)
    if count < k: s = mid + 1
    else: e = mid - 1
        
print(s)