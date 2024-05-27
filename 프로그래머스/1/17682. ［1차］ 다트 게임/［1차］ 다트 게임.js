function solution(dartResult) {
    let answer = [];
    let score = "";
    const SDTObj = {
        "S": 1,
        "D": 2,
        "T": 3
    }
    
    for (let v of dartResult){
        if (!isNaN(v)) score += v
        else if (/S|D|T/.test(v)) {
            answer.push(parseInt(score) ** SDTObj[v])
            score = ""
        } else if (v === "*") {
            if (answer.length > 1) answer[answer.length-2] *= 2
            answer[answer.length-1] *= 2
        } else if (v === "#") answer[answer.length-1] *= -1
    }
    return answer.reduce((a,c) => a + c, 0);
}