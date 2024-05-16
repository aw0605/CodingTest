function solution(arr, divisor) {
    const answer = arr.filter(v => !(v % divisor)).sort((a,b) => a-b)
    return answer.length? answer : [-1];
}