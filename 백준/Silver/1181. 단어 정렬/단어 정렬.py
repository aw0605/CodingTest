import sys
input = sys.stdin.readline

n = int(input())
arr = list(set(input().strip() for _ in range(n)))

arr.sort(key=lambda x: (len(x), x))

for v in arr:
    print(v)