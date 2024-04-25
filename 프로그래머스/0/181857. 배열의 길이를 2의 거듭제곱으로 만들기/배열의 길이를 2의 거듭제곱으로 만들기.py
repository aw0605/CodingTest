def solution(arr):
    i = 0;
    while len(arr) > pow(2,i): i += 1
    while pow(2,i) != len(arr): arr.append(0)
    return arr