def solution(my_string):
    answer = [0]*52
    all_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in my_string:
        answer[all_alpha.find(i)] += 1
    return answer