import sys
input = sys.stdin.readline

a = [2**i for i in range(32)]

q = int(input())

for i in range(q):
    n = int(input())
    print(1 if n in a else 0)