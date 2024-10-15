maxV = -1

for i in range(9):
    arr = list(map(int, input().split()))
    if max(arr) > maxV:
        maxV = max(arr)
        r,c = i+1, arr.index(maxV)+1

print(maxV)
print(r,c)
