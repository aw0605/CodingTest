import sys
input = sys.stdin.readline

n = int(input())
ans = 0
users = set()

for _ in range(n):
    cur = input().strip()
    if cur == "ENTER": users = set()
    else:
        if cur not in users:
            users.add(cur)
            ans += 1
            
print(ans)