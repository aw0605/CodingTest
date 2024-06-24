def solution(clothes):
    answer = 1
    
    clo_dict = {}
    for v in clothes:
        if v[1] in clo_dict: clo_dict[v[1]].append(v[0])
        else: clo_dict[v[1]] = [v[0]]
        
    for items in clo_dict.values():
        answer *= (len(items) + 1)
    
    return answer - 1