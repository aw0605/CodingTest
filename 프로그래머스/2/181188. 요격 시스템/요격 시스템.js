function solution(targets) {
    let answer = 0;
    targets.sort((a,b) => a[1] - b[1])
    
    let s, e = 0
    for (let target of targets) {
        if (target[0] >= e) {
            answer++
            e = target[1]
        }
    }
    
    return answer;
}