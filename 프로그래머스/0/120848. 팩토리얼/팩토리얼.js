function solution(n) {
    let answer = 0;
    let i = 1;
    for (let j = 1; j <= n; j++){
        i *= j
        if (i <= n) answer = j;
    }
    return answer;
}