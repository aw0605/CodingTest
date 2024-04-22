def solution(arr):
    answer = 0
    while True:
        arr_x = []
        for v in arr:
            if v >= 50 and v % 2 == 0: arr_x.append(v/2)
            elif v < 50 and v % 2 != 0: arr_x.append(v*2 + 1)
            else: arr_x.append(v)
                
        if arr == arr_x: return answer
        else:
            answer += 1
            arr = arr_x