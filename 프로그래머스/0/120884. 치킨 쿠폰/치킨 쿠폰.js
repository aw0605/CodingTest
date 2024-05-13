function solution(chicken) {
    let answer = 0;
    
    while (chicken > 9) {
        answer += Math.trunc(chicken / 10);
        chicken = chicken % 10 + Math.trunc(chicken / 10)
    }
    
    return answer;
}
