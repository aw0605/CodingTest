def divide(arr):
    size = len(arr)//2
    lu = [i[:size] for i in arr[:size]]
    ld = [i[:size] for i in arr[size:]]
    ru = [i[size:] for i in arr[:size]]
    rd = [i[size:] for i in arr[size:]]
    return lu, ld, ru, rd

def ziper(arr):
    size = len(arr)
    s = sum(sum(i) for i in arr)
    if s == size**2: return [1]
    elif s == 0: return [0]
    else:
        lu, ld, ru, rd = divide(arr)
        return ziper(lu) + ziper(ld) + ziper(ru) + ziper(rd)

def solution(arr):
    zip_res = ziper(arr)

    return [len(zip_res) - sum(zip_res), sum(zip_res)]