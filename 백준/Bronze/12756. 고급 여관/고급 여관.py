import sys
input = sys.stdin.readline

a1,l1 = map(int, input().split())
a2,l2 = map(int, input().split())

while True:
    if l1 <= 0 or l2 <= 0: break
    l1 -= a2
    l2 -= a1
    
if l1 <= 0 and l2 <= 0: print("DRAW")
else:
    if l1 > l2: print("PLAYER A")
    else: print("PLAYER B")