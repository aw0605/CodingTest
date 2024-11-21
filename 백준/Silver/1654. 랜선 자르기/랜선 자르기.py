import sys
input = sys.stdin.readline

k,n = map(int, input().split())
have = [int(input()) for _ in range(k)]
s,e = 1, max(have)

while s <= e:
    count = 0
    mid = (s + e) // 2
    for l in have: count += l // mid
    if count >= n: s = mid + 1
    else: e = mid - 1
        
print(e)