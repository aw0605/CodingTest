function collatz(k) {
    const arr = [k];
    while (k !== 1) {
        k = k % 2 === 0 ? k / 2 : k * 3 + 1;
        arr.push(k);
    }
    
    return arr;
}

function solution(k, ranges) {
    let answer = [];
    const ubak = collatz(k);
    let area = [];

    for (let i = 0; i < ubak.length - 1; i++) area.push((ubak[i] + ubak[i + 1]) / 2);

    const cumulativeArea = [0];
    for (let i = 0; i < area.length; i++) {
        cumulativeArea.push(cumulativeArea[i] + area[i]);
    }

    const n = cumulativeArea.length - 1;

    for (const [a, b] of ranges) {
        const endIndex = n + b;
        if (a > endIndex) answer.push(-1);
        else if (a === endIndex) answer.push(0);
        else answer.push(cumulativeArea[endIndex] - cumulativeArea[a]);
    }

    return answer;
}
