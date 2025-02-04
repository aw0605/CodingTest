n,r,c = map(int, input().split())

if not (r+c) % 2:
    for i in range(n):
        if not i % 2: print("v." * (n // 2) + 'v' * (n % 2))
        else: print(".v" * (n // 2) + '.' * (n % 2)) 
else:
    for i in range(n):
        if i % 2: print("v." * (n // 2) + 'v' * (n % 2))
        else: print(".v" * (n // 2) + '.' * (n % 2))