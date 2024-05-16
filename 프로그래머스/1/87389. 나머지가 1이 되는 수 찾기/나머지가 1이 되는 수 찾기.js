function solution(n) {
    let answer = [];
    for(let i = 2; i < n; i++){
        if (n % i === 1) answer.push(i)
    }
    return Math.min(...answer);
}