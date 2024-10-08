function makeMin(time) {
    const [hour, min] = time.split(":").map(v => Number(v));
    return hour * 60 + min;
}

function solution(book_time) {
    const timeArr = Array.from({ length: makeMin('23:59') + 10 }, () => 0);

    book_time.forEach((time, i) => {
        const [s, e] = time;
        let start = makeMin(s);
        const end = makeMin(e) + 9;

        for (start; start <= end; start++) timeArr[start]++;
    });

    return Math.max(...timeArr);
}