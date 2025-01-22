while True:
    n = input()
    if n == "0": break
    fn = n[::-1]
    print("yes" if n == fn else "no")