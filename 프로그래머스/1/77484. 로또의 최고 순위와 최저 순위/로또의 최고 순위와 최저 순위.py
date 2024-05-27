def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    curN = len([v for v in lottos if v in win_nums])
    zeroN = lottos.count(0)

    return [rank[curN+zeroN], rank[curN]]