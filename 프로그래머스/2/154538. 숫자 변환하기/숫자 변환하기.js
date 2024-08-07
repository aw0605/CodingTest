function solution(x, y, n) {
    if (x === y) return 0;
    const dp = {};
    let data = [x];
    dp[x] = 0;
    
    while (data.length) {
        const newData = [];
        for (const d of data) {
            for (const e of [d + n, d * 2, d * 3]) {
                if (e > y || dp[e]) continue;
                if (e === y) return dp[d] + 1;
                dp[e] = dp[d] + 1;
                newData.push(e);
            }
        }
        data = newData;
    }
    
    return -1;
}