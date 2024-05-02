const facto = (num) => num === 0? 1 : num * facto(num-1)

function solution(balls, share) {
    var answer = 0;
    return Math.round(facto(balls) / (facto(balls - share) * facto(share)));
}