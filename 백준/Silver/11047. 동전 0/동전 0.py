import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)

count = 0

for c in coins:
    count += k // c
    k = k % c
    
print(count)