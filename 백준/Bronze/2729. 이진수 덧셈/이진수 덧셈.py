import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a,b = input().split()
    ans = bin(int(a, 2) + int(b, 2))[2:]
    print(ans)