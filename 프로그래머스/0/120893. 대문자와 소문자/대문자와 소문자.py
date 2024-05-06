def solution(my_string):
    return ''.join(v.lower() if v.isupper() else v.upper() for v in my_string)