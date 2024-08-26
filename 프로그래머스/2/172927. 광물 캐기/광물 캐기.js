function solution(picks, minerals) {
    let answer = 0;
    const total = picks.reduce((a, b) => a + b, 0);  
    let num = total * 5;
    
    if (minerals.length > num) minerals = minerals.slice(0, num);
    
    let newMinerals = Array(Math.floor(minerals.length / 5) + 1).fill().map(() => [0, 0, 0]);
    
    for (let i = 0; i < minerals.length; i++) {
        if (minerals[i] === 'diamond') newMinerals[Math.floor(i / 5)][0] += 1;
        else if (minerals[i] === 'iron') newMinerals[Math.floor(i / 5)][1] += 1;
        else if (minerals[i] === 'stone') newMinerals[Math.floor(i / 5)][2] += 1;
    }
    
    newMinerals.sort((a, b) => b[0] - a[0] || b[1] - a[1] || b[2] - a[2]);
    
    for (let i = 0; i < newMinerals.length; i++) {
        const [dia, iron, stone] = newMinerals[i];
        for (let j = 0; j < picks.length; j++) {
            if (picks[j] > 0) {
                if (j === 0) {
                    picks[j] -= 1;
                    answer += dia + iron + stone;
                    break;
                } else if (j === 1) {
                    picks[j] -= 1;
                    answer += (5 * dia) + iron + stone;
                    break;
                } else if (j === 2) {
                    picks[j] -= 1;
                    answer += (25 * dia) + (5 * iron) + stone;
                    break;
                }
            }
        }
    }
    
    return answer;
}
