def solution(str_list, ex):
    return ''.join(v for v in str_list if ex not in v)