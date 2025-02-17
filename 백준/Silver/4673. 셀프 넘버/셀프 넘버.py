def selfNum(n):
    nums = list(str(n))
    res = n
    for v in nums: res += int(v)
    return res

arr = set()
for n in range(10000): arr.add(selfNum(n))
for i in range(1,10001):
    if i not in arr: print(i)