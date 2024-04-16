def solution(my_string, m, c):
    answer = ''
    result = []
    for i in range(len(my_string)//m):
        result.append(list(my_string[i*m:i*m+m]))
        
    for i in result:
        answer += i[c-1]
    return answer