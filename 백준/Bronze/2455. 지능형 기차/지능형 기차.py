total = 0
ans = 0

for _ in range(4):
    o,i = map(int, input().split())
    total += i - o
    ans = max(ans, total)
        
print(ans)