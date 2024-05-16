function solution(x, n) {
    let answer = [];
    for (let i = 0; i < n; i++){
        answer.push(i * x + x)
    }
    return answer;
}