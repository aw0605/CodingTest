import sys
input = sys.stdin.readline

arr = [input().strip() for _ in range(5)]
ans = []

for i, v in enumerate(arr):
    if "FBI" in v: ans.append(i+1)

print("HE GOT AWAY!" if not len(ans) else " ".join(map(str, ans)))