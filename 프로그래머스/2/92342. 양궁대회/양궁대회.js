function solution(n, info) {
    let answer = new Array(11).fill(0);
    let result = 0;

    function score(ryan) {
        let s = 0;
        for (let i = 0; i < 11; i++) {
            if (ryan[i] === 0 && info[i] === 0) continue;
            if (ryan[i] > info[i]) {
                s += 10 - i;
            } else {
                s -= 10 - i;
            }
        }
        return s;
    }

    function dfs(idx, left, ryan) {
        if (idx === -1 && left > 0) return;
        if (left === 0) {
            let s = score(ryan);
            if (result < s) {
                answer = ryan.slice();  // copy the array
                result = s;
            }
            return;
        }
        for (let i = left; i >= 0; i--) {
            ryan[idx] = i;
            dfs(idx - 1, left - i, ryan);
            ryan[idx] = 0;
        }
    }

    dfs(10, n, new Array(11).fill(0));
    return result !== 0 ? answer : [-1];
}
