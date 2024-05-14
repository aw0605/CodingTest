function solution(num, total) {
    let answer = []
    const sNum = Math.ceil(total / num) - Math.trunc(num / 2)
    for (let i = 0; i < num; i++){
        answer.push(i + sNum)
    }
    return answer;
}