s = input().upper()
setS = list(set(s))
arr = []

for v in setS:
    count = s.count(v)
    arr.append(count)

print("?" if arr.count(max(arr)) > 1 else setS[arr.index(max(arr))])