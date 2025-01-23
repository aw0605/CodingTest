import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(10)]

cur = 0 
for v in arr:
    cur += v
    if cur >= 100:
        if cur - 100 > 100 - (cur - v): cur -= v
        break

print(cur)