def solution(lottos, win_nums):
    curN = len([v for v in lottos if v in win_nums])
    zeroN = lottos.count(0)
    
    if curN + zeroN < 2: best = 6
    else: best = 7 - (curN+zeroN)
        
    if curN < 2: worst = 6
    else: worst = 7 - curN

    return [best, worst]