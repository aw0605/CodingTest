from collections import Counter

def solution(topping):
    split_count = 0
    topping_counter = Counter(topping)
    half_topping_set = set()
    
    for v in topping:
        half_topping_set.add(v)
        topping_counter[v] -= 1
        
        if topping_counter[v] == 0: topping_counter.pop(v)
        if len(half_topping_set) == len(topping_counter): split_count += 1
        
    return split_count