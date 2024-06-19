def solution(elements):
    comb = set()
    
    elLen = len(elements)
    elements = elements * 2
    
    for i in range(elLen):
        for j in range(elLen):
            comb.add(sum(elements[j:j+i+1]))
    
    return len(comb)