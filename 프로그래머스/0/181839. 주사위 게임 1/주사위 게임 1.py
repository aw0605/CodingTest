def solution(a, b):
    def isOdd(x): return x % 2 == 1
    
    if not isOdd(a) and not isOdd(b): return abs(a - b)
    elif isOdd(a) and isOdd(b): return a**2 + b**2
    else: return 2 * (a + b)
