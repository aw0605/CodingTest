x,y = input().split()

def Rev(n):
    return int(n[::-1])

print(Rev(str(Rev(x) + Rev(y))))