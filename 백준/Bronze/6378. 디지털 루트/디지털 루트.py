while True:
    n = input().strip()
    if n == "0": break
    while len(n) > 1:
        n = str(sum([int(v) for v in n]))
    print(n)