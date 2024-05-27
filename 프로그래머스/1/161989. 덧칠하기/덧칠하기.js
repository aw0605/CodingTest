function solution(n, m, section) {
    let answer = 0;
    let paint = 0;
    
    for (let v of section){
        if (paint < v){
            answer++
            paint = v + m - 1
        }
    }
    return answer;
}