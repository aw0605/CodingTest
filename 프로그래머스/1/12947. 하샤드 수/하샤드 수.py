def solution(x):
    xSum = sum(int(v) for v in str(x))
    return x % xSum == 0