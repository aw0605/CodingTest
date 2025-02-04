from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input()
    n,m = map(int, input().split())
    sj = deque(sorted(map(int, input().split())))
    sb = deque(sorted(map(int, input().split())))
    while sj and sb:
        if sj[0] >= sb[0]: sb.popleft()
        else: sj.popleft()
    if sj: print("S")
    elif sb: print("B")
    else: print("C")