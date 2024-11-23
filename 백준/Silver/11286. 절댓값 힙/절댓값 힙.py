import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    cur = int(input())
    if cur: heapq.heappush(hq, (abs(cur), cur))
    else:
        if not hq: print(0)
        else: print(heapq.heappop(hq)[1])