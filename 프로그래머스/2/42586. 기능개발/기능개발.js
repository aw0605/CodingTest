function solution(progresses, speeds) {
    let answer = [];

    while (speeds.length > 0) {
        for (let i in speeds) {
            if (progresses[i] < 100) progresses[i] += speeds[i];
        }

        let d = 0;
        while (progresses[0] >= 100) {
            progresses.shift();
            speeds.shift();
            d++;
        }
        
        if (d > 0) answer.push(d);
    }

    return answer;
}