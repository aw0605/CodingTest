s = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
ans = 0

for v in s:
    for i,w in enumerate(dial):
        if v in w: ans += i + 3
            
print(ans)
        

