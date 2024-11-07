from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [i+1 for i in range(n)]

ans = combinations(arr, m)

for comb in ans:
    print(*comb)