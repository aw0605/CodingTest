function solution(targets) {
    let answer = 0;
    targets.sort((a,b) => a[1] - b[1])
    let tmp = 0
    
    for (let target of targets) {
        if (target[0] < tmp) continue
        else {
            answer++
            tmp = target[1]
        }
    }
    
    return answer;
}