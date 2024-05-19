from itertools import combinations

def solution(number):
    answer = 0;
    for v in combinations(number,3):
        if not sum(v): answer+=1
    return answer
