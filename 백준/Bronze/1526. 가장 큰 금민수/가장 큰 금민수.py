n = int(input())

while True:
    flag = 1
    for s in str(n):
        if s != "4" and s != "7":
            flag = 0
            n -= 1
    if flag:
        print(n)
        break