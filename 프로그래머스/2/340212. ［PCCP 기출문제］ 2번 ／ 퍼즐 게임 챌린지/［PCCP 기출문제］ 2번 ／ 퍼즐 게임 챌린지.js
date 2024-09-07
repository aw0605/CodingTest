function solution(diffs, times, limit) {
    let left = 1, right = 100001;

    function solveTime(level) {
        let total = 0;

        for (let i = 0; i < diffs.length; i++) {
            const diff = diffs[i];
            const cur = times[i];

            if (diff <= level) total += cur;
            else {
                const mistakes = diff - level;
                const prev = times[i-1]
                
                total += mistakes * (prev + cur) + cur
            }
        }

        return total;
    }

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (solveTime(mid) <= limit) right = mid - 1;
        else left = mid + 1;
    }

    return left;
}
