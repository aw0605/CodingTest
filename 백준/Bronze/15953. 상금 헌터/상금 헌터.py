import sys
input = sys.stdin.readline

m1 = [0] + [500] + [300]*2 + [200]*3 + [50]*4 + [30]*5 + [10]*6
m2 = [0] + [512] + [256]*2 + [128]*4 + [64]*8 + [32]*16

t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    p1 = m1[a] if 1<= a <=21 else 0
    p2 = m2[b] if 1<= b <=31 else 0
    money = (p1 + p2) * 10000
    print(money)