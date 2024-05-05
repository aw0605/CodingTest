def solution(numbers):
    sortArr = sorted(numbers, reverse = True)
    return sortArr[0] * sortArr[1]