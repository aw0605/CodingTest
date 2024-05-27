function solution(N, stages) {
    let answer = [];
    for(let i = 1; i <= N; i++){
        let player = stages.filter((x) => x >= i).length;
        let fail = stages.filter((x) => x === i).length;
        answer.push([i, fail/player]);
    }
    answer.sort((a,b) => b[1] - a[1]);
    return answer.map((x) => x[0]);
}