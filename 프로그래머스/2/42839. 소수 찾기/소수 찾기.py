def isPrimeNumber(number):
    if number <= 1: return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:return False
    return True

def getAllCombination(numbers, numList, leftCipher):
    newNumList = [[]]
    for li in numList:
        for i in numbers:
            if i in li and li.count(i) <= numbers.count(i) - 1:
                tmp = li[:]
                tmp.append(i)
                newNumList.append(tmp)
            if i not in li:
                tmp = li[:]
                tmp.append(i)
                newNumList.append(tmp)

    leftCipher -= 1

    if leftCipher == 0: return newNumList
    else: return getAllCombination(numbers, newNumList, leftCipher)

def removeFirstZero(numList):
    for i, num in enumerate(numList):
        firstNumIsZero = bool()

        while True:
            if len(num) >= 2 and num[0] == '0': firstNumIsZero = True
            else:
                numList[i] = num
                break

            num = num[1:]

def getUnique2DList(numList):
    for i, val in enumerate(numList):
        tmp = str()
        for char in val: tmp += char
        numList[i] = tmp

    newList = list(set(numList))
    return newList

def solution(numbers):    
    availableAnswer = getAllCombination(numbers, [[]], len(numbers))
    del availableAnswer[0]
    removeFirstZero(availableAnswer)
    availableAnswer = getUnique2DList(availableAnswer)

    answer = 0
    for val in availableAnswer:
        if isPrimeNumber(int(val)): answer += 1

    return answer