function solution(array) {
    return ([...array.toString()].filter(v => v === "7")).length;
}