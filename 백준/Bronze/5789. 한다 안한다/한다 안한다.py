import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    mid = len(s)//2
    if s[mid-1] == s[mid]: print("Do-it")
    else: print("Do-it-Not")