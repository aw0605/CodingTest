import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x = list(input().strip())
    ans = ""
    for i in range(len(x)-1, 0, -1):
        if int(x[i]) >= 5:
            x[i-1] = str(int(x[i-1]) + 1)
        x[i] = "0"
    for s in x: ans += s
    print(ans) 