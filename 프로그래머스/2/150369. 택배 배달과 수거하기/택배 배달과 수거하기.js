function solution(cap, n, deliveries, pickups) {
    let answer = 0, d = 0, p = 0;
    let pos = n - 1;

    for (let i = n - 1; i >= 0; i--) {
        d += deliveries[i];
        p += pickups[i];

        while (d > cap || p > cap) {
            d -= cap;
            p -= cap;
            answer += 2 * (pos + 1);
            pos = i;
        }
    }

    if (d > 0 || p > 0) answer += 2 * (pos + 1);

    return answer;
}
