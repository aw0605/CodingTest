import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
ans = [n for n in arr if n > 0]

print(len(ans))