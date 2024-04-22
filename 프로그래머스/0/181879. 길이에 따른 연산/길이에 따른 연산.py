from functools import reduce
def solution(num_list):
    func = lambda a, b: a + b if (len(num_list) >= 11) else a * b
    return reduce(func, num_list)