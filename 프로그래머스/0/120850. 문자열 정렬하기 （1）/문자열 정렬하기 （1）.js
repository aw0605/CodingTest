function solution(my_string) {
    let numArr = [...my_string].filter(v => Math.floor(v) || Math.floor(v) === 0)
    return numArr.map(v => +v).sort((a, b) => a - b);
}