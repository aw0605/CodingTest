def solution(strArr):
    lenArr = [0] * 31
    for v in strArr: lenArr[len(v)] += 1
    return max(lenArr)