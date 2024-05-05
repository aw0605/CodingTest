def solution(my_string):
    gather = ["a", "e", "i", "o", "u"]
    return ''.join(v for v in my_string if v not in gather)