function solution(s) {
    let x = "";
    let count = 0;
    let answer = 0;
    
    for (let v of s) {
        if (!count) {
            answer++;
            x = v;
        }
        
        v === x ? count++ : count--;
    }
    
    return answer;
}