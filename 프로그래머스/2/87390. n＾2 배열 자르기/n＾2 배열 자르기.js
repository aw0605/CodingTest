function solution(n, left, right) {
    let answer = [];
    
    for (let i = left; i <= right; i++) {
        let l = Math.trunc(i/n);
        let r = i%n;
        answer.push(Math.max(l, r) + 1);
    }
    
    return answer;
}