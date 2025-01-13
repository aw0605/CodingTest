import sys
input = sys.stdin.readline

while True:
    a, *li = map(int, input().split())
    if a == 0: break
    n = 1
    for i in range(a):
        n = n * li[2*i] - li[2*i+1]
    print(n)