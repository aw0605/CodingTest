from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([key for _, key in clothes])
    answer = reduce(lambda x, y: x * (y+1), cnt.values(), 1) - 1
    return answer