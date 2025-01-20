n = int(input())
origin = n
ans = 0

while True:
    ten = n // 10
    one = n % 10
    num = one * 10 + (ten + one) % 10
    ans += 1
    if num == origin: break
    n = num

print(ans)