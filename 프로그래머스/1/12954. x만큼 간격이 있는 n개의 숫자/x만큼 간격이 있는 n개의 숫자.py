def solution(x, n):
    ans = [x]
    while len(ans) != n: ans.append(ans[-1] + x)
    return ans