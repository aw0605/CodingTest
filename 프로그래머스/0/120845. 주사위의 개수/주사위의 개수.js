function solution(box, n) {
    let [a,b,c] = box
    return Math.trunc(a / n) * Math.trunc(b / n) * Math.trunc(c / n);
}