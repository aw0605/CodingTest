n = int(input())

if n == 1: print('*')
else:
    for i in range(n):
        print("* "*n if not i%2 else " *"*n)