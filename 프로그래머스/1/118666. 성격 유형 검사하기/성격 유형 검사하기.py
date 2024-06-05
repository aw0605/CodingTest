def solution(survey, choices):
    answer = ''
    result = {
        "R": 0, "T": 0,
        "C": 0, "F": 0,
        "J": 0, "M": 0,
        "A": 0, "N": 0,
    }

    for v,c in zip(survey, choices):
        if c < 4: result[v[0]] += (4 - c)
        elif c > 4: result[v[1]] += (c - 4)
        else: continue
        
    types = list(result.keys())
    
    for l,r in zip(types[::2], types[1::2]):
        if result[l] < result[r]: answer += r
        else: answer += l
    
    return answer