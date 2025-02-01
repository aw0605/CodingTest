s = input()
n = len(s)

x = y = 0
for r in range(1, n//2 + 1):
    for c in range(r, n+1):
        if r * c == n: x,y = r,c
            
for i in range(x):
    for j in range(y):
        print(s[i+j*x], end="")