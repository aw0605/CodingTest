function solution(progresses, speeds) {
    let answer = [0];
    let rest = []
    for (let i = 0; i < speeds.length; i++){
        rest.push(Math.ceil((100 - progresses[i]) / speeds[i]))
    }
    
    let max = rest[0];

    for (let i = 0, j = 0; i< rest.length; i++){
        if(rest[i] <= max) answer[j] += 1;
        else {
            max = rest[i];
            answer[++j] = 1;
        }
    }

    return answer;
}