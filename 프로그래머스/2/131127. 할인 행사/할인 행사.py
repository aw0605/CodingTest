from collections import Counter

def solution(want, number, discount):
    answer = 0
    item_dict = {v: n for v,n in zip(want, number)}

    for i in range(len(discount)-9):
        if item_dict == Counter(discount[i:i+10]): answer += 1

    return answer