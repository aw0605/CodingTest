function solution(x) {
    const xSum = String(x).split("").map(v => +v).reduce((a,c) => a+c)
    return x % xSum? false : true;
}