from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
orders = deque(enumerate(map(int, input().split())))

ans = []

while orders:
    i, v = orders.popleft()
    ans.append(i+1)
    if v > 0: orders.rotate(-(v-1))
    else: orders.rotate(-v)
        
print(" ".join(map(str, ans)))