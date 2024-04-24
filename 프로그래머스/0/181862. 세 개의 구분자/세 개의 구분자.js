function solution(myStr) {
    let result = myStr.split(/a|b|c/).filter(v => v !== "")
    return result.length === 0? ["EMPTY"] : result
}