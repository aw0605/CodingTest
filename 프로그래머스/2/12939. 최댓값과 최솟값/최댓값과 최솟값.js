function solution(s) {
    const numArr = s.split(" ").map(v => +v)
    return `${Math.min(...numArr)} ${Math.max(...numArr)}`;
}