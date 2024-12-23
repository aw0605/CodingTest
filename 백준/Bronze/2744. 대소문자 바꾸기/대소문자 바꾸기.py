s = input().strip()

ans = ""
for v in s:
    if v.isupper(): ans += v.lower()
    else: ans += v.upper()
        
print(ans)