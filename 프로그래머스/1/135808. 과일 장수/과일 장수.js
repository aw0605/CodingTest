function solution(k, m, score) {
    let answer = 0
    let soldArr = score.sort((a,b) => a-b).slice(score.length%m)
    for (let i = 0; i < soldArr.length; i+=m){
        answer += soldArr[i] * m
    }
    return answer;
}