function solution(word) {
    const answer = {};
    let n = 0;
    function dfs(w) {
        if (w.length > 5) return;
        answer[w] = n;
        n++;
        for (let v of "AEIOU") {
            dfs(w + v);
        }
    }
    dfs("");
    return answer[word];
}