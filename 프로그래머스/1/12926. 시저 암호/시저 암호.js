function solution(s, n) {
    let answer = '';
    const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    const lower = "abcdefghijklmnopqrstuvwxyz"
    
    for (let v of s){
        if (v === " ") answer += v
        else {
            let Aa = upper.includes(v)? upper : lower;
            answer += Aa[(Aa.indexOf(v)+n) % 26] 
        }
    }
    return answer;
}