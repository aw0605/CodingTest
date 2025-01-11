import sys
input = sys.stdin.readline

n = int(input())
ans = 1
while n != 1:
    if not n % 2: n //= 2
    else: n = 3*n + 1
    ans += 1
    
print(ans)