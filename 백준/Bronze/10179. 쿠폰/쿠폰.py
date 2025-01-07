import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    price = float(input())
    ans = price * 0.8
    print(f"${ans:.2f}")
