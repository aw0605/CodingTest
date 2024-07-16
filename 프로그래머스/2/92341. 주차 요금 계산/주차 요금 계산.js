function solution(fees, records) {
    const answer = [];
    const parkingTime = {};
    
    records.forEach(v => {
        let [t, n, s] = v.split(' ');
        let [h, m] = t.split(':');
        t = (h * 1) * 60 + (m * 1);
        if (!parkingTime[n]) parkingTime[n] = 0;
        if (s === 'IN') parkingTime[n] += (1439 - t);
        if (s === 'OUT') parkingTime[n] -= (1439 - t);
    });
    
    for (let [n, t] of Object.entries(parkingTime)) {
        if (t <= fees[0]) t = fees[1];
        else t = Math.ceil((t - fees[0]) / fees[2]) * fees[3] + fees[1]
        answer.push([n, t]);
    }
    
    return answer.sort((a, b) => a[0] - b[0]).map(v => v[1]);
}