from collections import Counter
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [input().strip() for _ in range(n)]
mArr = [v for v in arr if len(v) >= m]
counter = Counter(mArr)

ans = list(set(mArr))

ans.sort(key=lambda x: (-counter[x], -len(x), x))

print("\n".join(ans))