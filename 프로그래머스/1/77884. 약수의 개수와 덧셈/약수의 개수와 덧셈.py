def solution(left, right):
    return sum(-v if int(v**0.5)**2 == v else v for v in range(left, right+1))