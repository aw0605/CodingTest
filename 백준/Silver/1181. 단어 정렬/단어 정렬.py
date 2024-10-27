import sys
input = sys.stdin.readline

n = int(input())
arr = list(set(input().strip() for _ in range(n)))

arr.sort()
arr.sort(key=len)

for v in arr:
    print(v)