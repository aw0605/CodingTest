import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    v = int(input())
    arr = [int(input()) for _ in range(v)]
    maxN = [0,0]
    for n in arr:
        cnt = arr.count(n)
        if maxN[0] < cnt or (maxN[0] == cnt and maxN[1] > n): maxN = [cnt, n]
    print(maxN[1])