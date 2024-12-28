while True:
    try:
        total = sum(list(map(int, input().split())))
        if total == 4: print("E")
        elif total == 3: print("A")
        elif total == 2: print("B")
        elif total == 1: print("C")
        else: print("D")
    except EOFError:
        break
