import sys

n = int(sys.stdin.readline())
n //= 4
ans = ""

for i in range(n):
    ans += "long "

print(ans + "int")