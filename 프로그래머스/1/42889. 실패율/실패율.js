function solution(N, stages) {
    let answer = [];
    let player = stages.length;
    let clearArr = new Array(N+1).fill(0);
    
    for (let v of stages) clearArr[v-1]++
    
    for (let i = 0; i < N; i++){
        if (player === 0) answer.push([i+1, 0]);
        else answer.push([i+1, clearArr[i] / player]);
        player -= clearArr[i]
    }
    
    return answer.sort((a,b) => {
        if(b[1] !== a[1]) return b[1] - a[1];
        else return a[0] - b[0]
    }).map(v => v[0]);
}