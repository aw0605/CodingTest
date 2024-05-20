def solution(sizes):
    w = []
    h = []
    
    for v in sizes:
        w.append(max(v))
        h.append(min(v))
    
    return max(w) * max(h)