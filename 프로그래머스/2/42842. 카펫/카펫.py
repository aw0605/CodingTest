def solution(brown, yellow):
    total = brown + yellow
    
    for v in range(3, int(total**0.5)+1):
        if total % v == 0:
            h = int(total / v)
            if brown == (h + v - 2) * 2: return [h,v]
        
    return []