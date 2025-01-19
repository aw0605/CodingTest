n = int(input())

for _ in range(n):print("@" * (n * 5))
for _ in range((n*5)-(2*n)):print("@"*n)
for _ in range(n):print("@" * (n * 5))