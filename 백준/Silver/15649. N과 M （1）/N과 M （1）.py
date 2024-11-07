from itertools import permutations
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [i+1 for i in range(n)]

ans = permutations(arr, m)

for comb in ans:
    print(" ".join(map(str, comb)))

