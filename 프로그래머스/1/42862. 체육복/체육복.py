def solution(n, lost, reserve):
    setLost = set(lost) - set(reserve)
    setReserve = set(reserve) - set(lost)
    
    for v in sorted(setReserve):
        if v-1 in setLost: setLost.remove(v-1)
        elif v+1 in setLost: setLost.remove(v+1)
            
    return n - len(setLost)