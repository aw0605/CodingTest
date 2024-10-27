import sys
input = sys.stdin.readline

n = input().strip()
sort_num = sorted(n, reverse=True)

print("".join(sort_num))