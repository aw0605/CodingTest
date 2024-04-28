def solution(arr, k):
    return [v + k if k % 2 == 0 else v * k for v in arr]