n = input()

if len(n) == 1: 
    print("NO")
    exit()
    
for i in range(len(n)):
    a,b = n[:i+1],n[i+1:]
    m1 = m2 = 1
    for j in a: m1 *= int(j)
    for j in b: m2 *= int(j)
    if m1 == m2:
        print("YES")
        exit()
        
print("NO")