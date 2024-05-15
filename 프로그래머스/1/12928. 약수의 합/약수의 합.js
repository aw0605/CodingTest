function solution(n) {
    let answer = n;
    for (let i = 1; i < Math.trunc(n/2)+1; i++){
        if (n % i === 0) answer += i
    }
    return answer;
}