correct = [1, 1, 2, 2, 2, 8]
arr = map(int, input().split())

ans = [a-b for a,b in zip(correct,arr)]

for v in ans:
    print(v, end=" ")


