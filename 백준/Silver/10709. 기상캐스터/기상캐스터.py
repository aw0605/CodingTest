import sys
input = sys.stdin.readline

h, w = map(int, input().split())
for _ in range(h):
    row = input().strip()
    ans = []
    last = -1
    for i in range(w):
        if row[i] == "c":
            ans.append(0)
            last = i
        else: ans.append(i - last if last != -1 else -1)
    
    print(*ans)