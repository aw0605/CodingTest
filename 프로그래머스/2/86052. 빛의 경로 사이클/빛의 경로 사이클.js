function solution(grid) {
    const answer = [];
    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    const visit = Array.from({ length: grid.length }, () => 
        Array.from({ length: grid[0].length }, () => Array(4).fill(0))
    );

    function pathfind(r, c, d) {
        let count = 0;
        while (!visit[r][c][d]) {
            visit[r][c][d] = 1;
            count++;
            if (grid[r][c] === 'L') {
                d = (d + 3) % 4; // equivalent to (d - 1) % 4
            } else if (grid[r][c] === 'R') {
                d = (d + 1) % 4;
            }
            r = (r + directions[d][0] + grid.length) % grid.length;
            c = (c + directions[d][1] + grid[0].length) % grid[0].length;
        }
        return count;
    }

    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[0].length; c++) {
            for (let d = 0; d < 4; d++) {
                if (visit[r][c][d]) continue;
                answer.push(pathfind(r, c, d));
            }
        }
    }

    return answer.sort((a, b) => a - b);
}
