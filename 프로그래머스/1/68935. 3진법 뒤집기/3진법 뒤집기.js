function solution(n) {
    let threeNR = [];
    let answer = 0;
    while (n / 3 !== 0){
        threeNR.push(n % 3)
        n = Math.trunc(n / 3)
    }
    for(let i = 0; i < threeNR.length; i++){
        answer += ([...threeNR].reverse())[i] * 3**i
    }
    return answer;
}