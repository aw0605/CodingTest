import sys
input = sys.stdin.readline

n = int(input())
seats = input()

cnt = seats.count("LL")

print(n if cnt <= 1 else n - cnt + 1)