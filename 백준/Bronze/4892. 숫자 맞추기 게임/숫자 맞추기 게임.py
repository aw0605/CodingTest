import sys
input = sys.stdin.readline

def isOdd(num):
    if num % 2 == 0: return False
    return True

i = 1
while True:
    n0 = int(input())
    if n0 == 0: break
    n1 = 3 * n0
    n2 = (n1 + 1) // 2 if isOdd(n1) else n1 // 2
    n3 = 3 * n2
    n4 = n3 // 9
    res = "odd" if isOdd(n1) else "even"
    print(f"{i}. {res} {n4}")
    i += 1