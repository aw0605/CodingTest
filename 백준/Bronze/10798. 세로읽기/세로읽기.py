arr = [input() for _ in range(5)]
ans = ""

max_len = max(len(row) for row in arr)

i = 0
while i < max_len:
    for j in range(5):
        if i < len(arr[j]):
            ans += arr[j][i]
    i += 1

print(ans)
