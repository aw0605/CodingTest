function solution(n, words) {
    let answer = 0;
    
    words.reduce((a, c, i) => {
        answer = answer || ((words.slice(0, i).indexOf(c) !== -1 || a !== c[0]) ? i : answer);
        return c[c.length-1];
    }, "")

    return answer ? [answer%n+1, Math.floor(answer/n)+1] : [0,0];
}