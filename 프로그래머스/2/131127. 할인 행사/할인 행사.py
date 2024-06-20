from collections import Counter

def solution(want, number, discount):
    answer = 0
    item_dict = {v: n for v,n in zip(want, number)}

    for i in range(len(discount)-sum(number)+1):
        if item_dict == Counter(discount[i:i+sum(number)]): answer += 1

    return answer