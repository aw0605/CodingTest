def solution(arr):
    if 2 not in arr: return [-1]
    idx = []
    for i,v in enumerate(arr):
        if v == 2: idx.append(i)
    return arr[idx[0]:idx[-1]+1]