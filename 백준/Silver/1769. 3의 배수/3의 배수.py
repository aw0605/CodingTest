n = list(map(int, input()))

cnt = 0
while len(n) > 1:
    res = str(sum(n))
    n = list(map(int, res))
    cnt += 1
    
last = sum(n) if cnt else n[0]
    
print(cnt)
print("YES" if not last % 3 else "NO")