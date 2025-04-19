import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    l = int(len(s) ** 0.5)
    res = ""
    for i in range(l, 0, -1):
        for j in range(i, len(s)+1, l):
            res += s[j-1]
    print(res)