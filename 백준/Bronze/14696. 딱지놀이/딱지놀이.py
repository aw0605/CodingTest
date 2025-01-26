import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    an, *a = map(int, input().split())
    bn, *b = map(int, input().split())
    for i in range(4,0,-1):
        if a.count(i) > b.count(i):
            print("A")
            break
        elif a.count(i) < b.count(i):
            print("B")
            break
    else: print("D")