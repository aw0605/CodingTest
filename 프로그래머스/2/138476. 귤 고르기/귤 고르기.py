def solution(k, tangerine):
    answer = 0
    tang_dict = {}
    for v in tangerine:
        if v in tang_dict: tang_dict[v] += 1
        else: tang_dict[v] = 1 
    tang_dict = sorted(tang_dict.values(), reverse=True)
    
    for i in tang_dict:
        k -= i
        answer += 1
        if (k <= 0): break
        
    return answer