function solution(fees, records) {
    let answer = [];
    let parkDict = {};
    const [dt, df, at, af] = fees;

    records.forEach(v => {
        let [t, n, s] = v.split(" ");
        let [h, m] = t.split(":").map(Number);
        t = h * 60 + m;

        if (!parkDict[n]) {parkDict[n] = [0, t, s];}
        else {
            if (s === "IN") {
                parkDict[n][1] = t;
                parkDict[n][2] = s;
            } else {
                parkDict[n][0] += t - parkDict[n][1];
                parkDict[n][2] = s;
            }
        }
    });

    Object.keys(parkDict).forEach(n => {
        let [total, last, s] = parkDict[n];
        if (s === "IN") {
            total += 1439 - last;
            parkDict[n][2] = "OUT";
        }

        let f = df;
        if (total > dt) f += Math.ceil((total - dt) / at) * af;
        answer.push([n, f]);
    });

    answer.sort((a, b) => a[0].localeCompare(b[0]));
    return answer.map(([n, f]) => f);
}
