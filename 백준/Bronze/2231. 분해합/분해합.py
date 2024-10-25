n = int(input())
ans = 0

for i in range(1, n):
    num = i + sum(map(int, str(i)))
    if num == n:
        ans = i
        break

print(ans if ans != 0 else 0)