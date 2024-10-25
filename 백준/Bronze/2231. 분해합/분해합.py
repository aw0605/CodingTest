n = int(input())
strN = str(n)

i = max(1, n - 9 * len(strN))
ans = 0

while i < n:
    num_sum = i + sum(map(int, str(i)))
    if num_sum == n:
        ans = i
        break
    i += 1

print(ans)
