function solution(n) {
    if (n % 2 !== 0) return 0;

    let i = 0;
    let dp = [1];
    let sum = 0;
    for(i = 2; i <= n; i += 2) {
        dp[i] = (dp[i-2] * 3 + sum * 2) % 1000000007;
        sum += dp[i-2];
    }

    return dp[n] % 1000000007;
}