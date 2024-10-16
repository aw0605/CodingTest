n = int(input())
money = [25, 10, 5, 1]

for _ in range(n):
    change = int(input())
    ans = []
    for v in money:
        ans.append(change//v)
        change %= v
    print(*ans)
        