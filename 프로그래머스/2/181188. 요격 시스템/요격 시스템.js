function solution(targets) {
    let answer = 1;
    let len = targets.length;
    targets.sort((a,b) => a[0] === b[0] ? b[0] - a[0] : a[0] - b[0])
    
    let l = targets[0][0]
    let r = targets[0][1]
    
    for (let i =1; i<len; i++) {
        if (r > targets[i][0]){
            if (r > targets[i][1]) r = targets[i][1]
        } else {
            answer++;
            r = targets[i][1]
        }
    }
    
    return answer
}