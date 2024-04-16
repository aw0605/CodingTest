def solution(my_string, s, e):
    result = my_string[s:e+1][::-1]
    return my_string.replace(my_string[s:e+1], result)