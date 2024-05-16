function solution(x) {
    const xSum = String(x).split("").reduce((a,c) => +a + +c)
    return !(x % xSum);
}