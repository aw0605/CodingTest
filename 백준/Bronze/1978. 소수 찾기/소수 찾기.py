n = int(input())
nums = list(map(int, input().split()))
ans = 0

for v in nums:
    if v == 1: continue
    for i in range(2, int(v ** 0.5) + 1):
        if v % i == 0: break
    else: ans += 1

print(ans)
        
