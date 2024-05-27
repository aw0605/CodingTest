function solution(n, m, section) {
    let answer = 0;
    const arr = new Array(n).fill(1);

    section.forEach(v => arr[v-1] = 0);

    section.map(v => {
        if (!arr[v-1]) {
            arr.fill(1, v-1, v+m-1);
            answer++
        }
    })
    return answer
}