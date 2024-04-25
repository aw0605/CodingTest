def solution(arr, n):
    for i,v in enumerate(arr):
        if len(arr) % 2 != i % 2: arr[i] = v + n
    return arr