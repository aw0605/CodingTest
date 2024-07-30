import math
from itertools import permutations

def isPrime(n):
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def solution(numbers):
    answer = set()
    nums = list(numbers)
    
    def get_permutation(arr, fix):
        for i in range(len(arr)):
            copy = arr[:i] + arr[i+1:]
            newN = int(fix + arr[i])
            if newN not in answer and isPrime(newN): answer.add(newN)
            get_permutation(copy, fix + arr[i])
    
    get_permutation(nums, '')
    return len(answer)

