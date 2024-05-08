function solution(s) {
    let answer = [];
    for (let v of s){
        if (s.indexOf(v) === s.lastIndexOf(v)) answer.push(v)
    }
    return answer.sort().join("");
}