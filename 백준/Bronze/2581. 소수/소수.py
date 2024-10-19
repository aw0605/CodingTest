def isPrime(num):
    if num == 1: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

m = int(input())
n = int(input())
arr = []

for num in range(m, n + 1):
    if isPrime(num): arr.append(num)

print(-1) if len(arr) == 0 else print(f"{sum(arr)}\n{min(arr)}")

