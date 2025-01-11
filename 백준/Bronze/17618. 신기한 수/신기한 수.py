n = int(input())
ans = 0
for i in range(1, n+1):
    j = sum([int(k) for k in str(i)])
    if not i % j: ans += 1
print(ans)