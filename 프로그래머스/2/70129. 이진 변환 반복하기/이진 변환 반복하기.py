def solution(s):
    number, zero = 0,0
    
    while s != "1":
        number += 1
        zero += s.count("0")
        s = bin(s.count("1"))[2:]
        
    return [number, zero]