nums = list(map(int, input().split()))
ans = sum([n ** 2 for n in nums]) % 10
print(ans)