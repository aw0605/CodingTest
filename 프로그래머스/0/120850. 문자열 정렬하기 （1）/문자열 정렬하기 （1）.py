def solution(my_string):
    return sorted([int(v) for v in my_string if v in "0123456789"])