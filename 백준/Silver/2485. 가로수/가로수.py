from math import gcd
import sys

data = sys.stdin.read().splitlines()
n = int(data[0])
arr = [int(data[i]) for i in range(1, n + 1)]
dif = [arr[i + 1] - arr[i] for i in range(n - 1)]

gcdN = dif[0]
for i in range(1, len(dif)):
    gcdN = gcd(gcdN, dif[i])

ans = sum(v // gcdN - 1 for v in dif)

print(ans)
