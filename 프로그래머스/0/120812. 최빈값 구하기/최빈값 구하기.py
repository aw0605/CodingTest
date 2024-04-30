from collections import Counter

def solution(array):
    a = Counter(array).most_common(2)
    if len(a) == 1:
        return a[0][0]
    if a[0][1] == a[1][1]:
        return -1
    return a[0][0]