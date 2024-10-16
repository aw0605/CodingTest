import sys
input = sys.stdin.readline

n = int(input())
money = [25, 10, 5, 1]

for _ in range(n):
    change = int(input())
    ans = []
    for v in money:
        count, change = divmod(change, v)
        ans.append(count)
    print(*ans)
        