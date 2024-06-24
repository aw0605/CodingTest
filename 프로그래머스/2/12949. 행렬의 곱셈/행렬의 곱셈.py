def solution(arr1, arr2):
     return [[sum(a*b for a, b in zip(A1,A2)) for A2 in zip(*arr2)] for A1 in arr1]