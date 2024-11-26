from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
F = Counter(arr)

ans = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and F[arr[stack[-1]]] < F[arr[i]]: ans[stack.pop()] = arr[i]
    stack.append(i)

print(*ans)