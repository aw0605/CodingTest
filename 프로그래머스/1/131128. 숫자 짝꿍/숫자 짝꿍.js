function solution(X, Y) {
    let answer = ''

    for(let n = 0 ; n <= 9 ; n++) {
        const xDupNum = [...X].filter(v => +v === n).length
        const YDupNum = [...Y].filter(v => +v === n).length
        answer += String(n).repeat(Math.min(xDupNum, YDupNum))
    }
    
    if (answer === '') return "-1"
    if (+answer === 0) return "0"
    return answer.split("").sort((a,b) => +b - +a).join("")
}