def solution(arr1, arr2):
    len1, len2 = len(arr1), len(arr2)
    if len1 != len2: return 1 if len1 > len2 else -1
    else: 
        sum1, sum2 = sum(arr1), sum(arr2)
        if sum1 == sum2: return 0
        else: return 1 if sum1 > sum2 else -1