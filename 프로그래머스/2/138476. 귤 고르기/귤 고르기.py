import collections

def solution(k, tangerine):
    answer = 0
    tang_dict = collections.Counter(tangerine)

    for v in sorted(tang_dict.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0: break
        
    return answer