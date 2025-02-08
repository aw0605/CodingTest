def solution(n):
    ans = 0
    arr = list(str(n))
    for v in arr: ans += int(v)
    return ans