def solution(arr, flag):
    X = []
    for i,v in enumerate(flag):
        if v: X.extend([arr[i]] * (arr[i] * 2))
        else: del X[-arr[i]:]
    return X