def solution(my_string, num1, num2):
    strArr = list(my_string)
    strArr[num1], strArr[num2] = strArr[num2], strArr[num1]
    return ''.join(strArr)