function solution(n) {
    return String(n).split("").map(v => +v).reverse();
}