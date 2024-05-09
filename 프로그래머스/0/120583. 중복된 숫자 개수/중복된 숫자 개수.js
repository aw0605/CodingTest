function solution(array, n) {
    let answer = 0;
    for (let v of array){
        if (v === n) answer++
    }
    return answer;
}