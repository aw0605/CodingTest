def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        v12 = bin(i|j)[2:].zfill(n)
        v12 = v12.replace("1", "#")
        v12 = v12.replace("0", " ")
        answer.append(v12)
    return answer