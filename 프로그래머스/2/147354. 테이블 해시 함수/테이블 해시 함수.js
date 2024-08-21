function solution(data, col, row_begin, row_end) {
    data = data.sort((a, b) => {
        if(a[col-1] === b[col-1]) return b[0] - a[0];
        return a[col-1] - b[col-1];
    });

    const result = [];
    for(let i=row_begin; i<=row_end; i++) {
        const row = data[i-1];
        const value = row.reduce((a, c) => {
            return a + (c % i);
        }, 0);

        result.push(value);
    }

    return result.reduce((a, c) => {
        if(a === null) return c;
        return a^c;
    }, null);
}