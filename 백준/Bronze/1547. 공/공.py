import sys
input = sys.stdin.readline

n = int(input())

cups = [0,1,2,3]
for _ in range(n):
    a,b = map(int, input().split())
    cups[a], cups[b] = cups[b], cups[a]

print(cups.index(1))