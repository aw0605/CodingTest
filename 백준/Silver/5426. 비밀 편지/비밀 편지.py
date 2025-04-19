import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    l = int(len(s) ** 0.5)
    arr = [s[i:i+l] for i in range(0, len(s), l)]
    for i in range(l-1,-1,-1):
        for j in range(l):
            print(arr[j][i], end="")
    print("")