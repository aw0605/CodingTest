from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    sort_counter = sorted(counter.values(), reverse = True)
    types = 0
    total = 0
    
    for count in sort_counter:
        total += count
        types += 1
        if total >= k: break
    
    return types