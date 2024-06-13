function solution(s){
    let answer = 0
    
    for (let v of s) {
        answer += v === "("? 1 : -1
        if (answer < 0) return false
    }
    
    return answer === 0? true : false;
}