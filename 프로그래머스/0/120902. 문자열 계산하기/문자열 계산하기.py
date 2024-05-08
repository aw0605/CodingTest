def solution(my_string):
    strArr = my_string.split()
    answer = int(strArr[0])
    for i in range(1,len(strArr),2):
        if strArr[i] == '+':
            answer += int(strArr[i+1])
        else:
            answer -= int(strArr[i+1])
    return answer