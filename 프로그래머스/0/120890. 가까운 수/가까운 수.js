function solution(array, n) {
    let answer = []
    array.sort((a,b) => a - b).map(v => answer.push(Math.abs(v - n)))
    return array[answer.indexOf(Math.min(...answer))];
}