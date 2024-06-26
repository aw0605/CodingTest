function solution(progresses, speeds) {
    let answer = [];
    let rest = [];
    for (let i = 0; i < speeds.length; i++){
        rest.push(Math.ceil((100 - progresses[i]) / speeds[i]))
    }
    
    let before = rest[0];
    let d = 1;
    for (let i = 1; i < rest.length; i++) {
        if (rest[i] <= before) d++;
        else {
            answer.push(d);
            d = 1;
            before = rest[i];
        }
    }
    answer.push(d)
    
    return answer;
}