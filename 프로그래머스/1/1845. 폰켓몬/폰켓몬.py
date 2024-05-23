def solution(nums):
    uniqNums = list(set(nums))
    return len(nums)//2 if len(nums)//2 < len(uniqNums) else len(uniqNums)