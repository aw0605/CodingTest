def solution(s):
    i, zero = 0,0
    
    while s != "1":
        i += 1
        one = s.count("1")
        zero += len(s) - one
        s = bin(one)[2:]
        
    return [i,zero]