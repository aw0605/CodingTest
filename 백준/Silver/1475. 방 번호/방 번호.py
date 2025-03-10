n = input()

ans = [0] * 10
for v in n:
    v = int(v)
    if v == 6 or v == 9:
        if ans[6] <= ans[9]: ans[6] += 1
        else: ans[9] += 1
    else: ans[v] += 1

print(max(ans))