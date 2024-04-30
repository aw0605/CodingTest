from functools import reduce

def solution(numbers):
    return reduce(lambda a,c: a + c, numbers) / len(numbers)