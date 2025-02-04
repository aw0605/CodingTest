import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input()
    n,m = map(int, input().split())
    sj = list(map(int, input().split()))
    sb = list(map(int, input().split()))
    sj.sort()
    sb.sort()
    while sj and sb:
        if sj[0] >= sb[0]: sb.pop(0)
        else: sj.pop(0)
    if sj: print("S")
    elif sb: print("B")
    else: print("C")