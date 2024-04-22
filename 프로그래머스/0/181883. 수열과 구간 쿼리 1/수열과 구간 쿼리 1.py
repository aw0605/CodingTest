def solution(arr, queries):
    for v in queries:
        [s,e] = v
        for i in range(s,e+1):
            arr[i] += 1
    return arr