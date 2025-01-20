import sys
input = sys.stdin.readline

n = int(input())
ans = list(input().strip())
if n == 1:
    print("".join(ans))
    exit()
arr = [input().strip() for _ in range(n-1)]

for v in arr:
    for j in range(len(ans)):
        if ans[j] != v[j]: ans[j] = "?"
            
print("".join(ans))