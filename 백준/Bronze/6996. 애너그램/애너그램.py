import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a,b = input().strip().split()
    if sorted(a) == sorted(b): print(f"{a} & {b} are anagrams.")
    else: print(f"{a} & {b} are NOT anagrams.")