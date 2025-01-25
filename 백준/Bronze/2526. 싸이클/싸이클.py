n,p = map(int, input().split())

res = []
a = n
while True:
    a = (a * n) % p
    if a in res: 
        print(len(res) - res.index(a))
        exit()
    res.append(a)