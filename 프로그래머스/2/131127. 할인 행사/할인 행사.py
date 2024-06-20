from collections import Counter

def solution(want, number, discount):
    item_dict = {v: n for v, n in zip(want, number)}
    total = sum(number)
    answer = 0
    
    for i in range(len(discount) - total+1):
        sale_dict = Counter(discount[i:i+total])
        
        for v in want:
            if item_dict[v] == sale_dict[v]: sale_dict[v] = 0
            else: break

        if sum(sale_dict.values()) == 0: answer += 1 
    
    return answer