def solution(array):
    answerArr = [0] * (max(array)+1)
    for v in array:
        answerArr[v] += 1
    
    if answerArr.count(max(answerArr)) != 1: return -1 
    else: return answerArr.index(max(answerArr))