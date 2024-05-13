def solution(score):
    averageArr = [sum(v)/2 for v in score]
    sortArr = sorted(averageArr, reverse = True)
    return [sortArr.index(v) + 1 for v in averageArr]