function solution(n) {
    const tri = Array.from({ length: n }, (_, i) => Array(i + 1).fill(0));
    let x = -1, y = 0;
    let num = 1;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i; j++) {
            if (i % 3 === 0) x++;
            else if (i % 3 === 1) y++;
            else {
                x--;
                y--;
            }
            tri[x][y] = num;
            num++;
        }
    }

    return tri.flat();
}
