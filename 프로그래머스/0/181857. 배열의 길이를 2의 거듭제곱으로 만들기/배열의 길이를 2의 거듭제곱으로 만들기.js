function solution(arr) {
    let i = 0;
    while (Math.pow(2, i) < arr.length) i++;
    return [...arr, ...new Array(Math.pow(2, i) - arr.length).fill(0)];
}