function solution(s1, s2) {
    var answer = 0;
    for (let x of s1){
        for (let y of s2){
            if (x === y) answer++
        }
    }
    return answer;
}