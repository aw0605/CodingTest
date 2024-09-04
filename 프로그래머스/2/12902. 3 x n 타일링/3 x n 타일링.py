def solution(n):
    if n % 2 != 0: return 0

    dp = [0] * (n + 1)
    dp[0] = 1
    total = 0

    for i in range(2, n + 1, 2):
        dp[i] = (dp[i-2] * 3 + total * 2) % 1000000007
        total += dp[i-2]

    return dp[n] % 1000000007
