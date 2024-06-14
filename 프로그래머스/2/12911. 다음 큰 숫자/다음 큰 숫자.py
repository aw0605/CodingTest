def solution(n):
    i = n+1
    nCount = bin(n).count("1")
    
    while True:
        if nCount == bin(i).count("1"): return i
        i += 1