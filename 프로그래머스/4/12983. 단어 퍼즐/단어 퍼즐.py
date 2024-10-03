def solution(strs, t):
    n = len(t)
    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    sizes = set(len(s) for s in strs)

    for i in range(1, n + 1):
        for s in sizes:
            if (i - s >= 0 and t[i - s : i] in strs):
                dp[i] = min(dp[i], dp[i - s] + 1)
                
    return dp[n] if dp[n] < float("inf") else -1