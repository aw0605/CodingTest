from itertools import combinations

def solution(nums):
    answer = 0
    combArr = list(combinations(nums, 3))
    
    for v in combArr:
        for i in range(2,int(sum(v)**0.5)+1):
            if sum(v) % i == 0: break
        else: answer+=1

    return answer