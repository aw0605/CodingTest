n, l, d = map(int,input().split())

l += 5
playing = 0
cur = d
for i in range(n):
    playing += l
    while True:
        if cur < playing-5: cur += d
        else: break
    if playing - 5 <= cur < playing: break
        
print(cur)