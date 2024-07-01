function solution(priorities, location) {
    let arr = priorities.map((v, i) => {
        return {val: v, idx: i};
    });

    let answer = [];

    while (arr.length > 0) {
        let cur = arr.shift();
        let notMax = arr.some(v => v.val > cur.val);
        if (notMax) arr.push(cur);
        else answer.push(cur);
    }

    return answer.findIndex(v => v.idx === location) + 1;
}