import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
s = 210
for _ in range(n):
    t, z = input().split()
    s -= int(t)
    if s <= 0: 
        print(k)
        break
    if z == "T": 
        k = 1 if k == 8 else k + 1