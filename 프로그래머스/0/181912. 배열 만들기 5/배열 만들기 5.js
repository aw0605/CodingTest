function solution(intStrs, k, s, l) {
    let result = ""
    let answer = [];
    intStrs.forEach((Str) => {
        result = Number(Str.slice(s, s+l))
        if(result > k){
            answer.push(result)
        }
    })
    return answer;
}