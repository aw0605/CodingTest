def solution(array):
    arrStr = ''.join(str(v) for v in array)
    return len([v for v in arrStr if v == "7"])