function solution(n, lost, reserve) {
    const student = {};
    let answer = 0;
    
    for (let i = 1; i <= n; i++) student[i] = 0;
    
    lost.forEach(v => student[v] -= 1);
    reserve.forEach(v => student[v] += 1);

    for (let i = 1; i <= n; i++) {
        if (student[i] === -1) {
            if (student[i - 1] === 1) {
                student[i - 1]--;
                student[i]++;
            } else if (student[i + 1] === 1) {
                student[i + 1]--;
                student[i]++;
            }
        }
    }
    
    for (let k in student) {
        if (student[k] >= 0) answer++;
    }
    
    return answer;
}
