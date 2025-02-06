import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    v = int(input())
    cnt = [0] * 1001
    for _ in range(v):
        cnt[int(input())] += 1
    most = max(cnt)
    print(cnt.index(most))