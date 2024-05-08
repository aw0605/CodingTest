def solution(num, k):
    numArr = list(str(num))
    return numArr.index(str(k)) + 1 if str(k) in numArr else -1