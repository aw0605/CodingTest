import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0: break
    ans = []
    maxH = 0
    for _ in range(n):
        a,b = input().strip().split()
        b = float(b)
        if b > maxH:
            maxH = b
            ans = [a]
        elif b == maxH: ans.append(a)
    print(" ".join(ans))