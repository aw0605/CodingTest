def solution(arr1, arr2):
    return [[sum(a*b for a, b in zip(A1,A2)) for A2 in zip(*arr2)] for A1 in arr1]
    # for A2 in zip(*arr2): 풀어서 행의 요소를 열별로 그룹화
    # [[5, 4, 3], [2, 4, 1], [3, 1, 1]] => [[5,2,3],[4,4,1],[3,1,1]]