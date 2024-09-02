function solution(land) {
    const n = land.length, m = land[0].length;
    const dx = [0, 0, 1, -1], dy = [1, -1, 0, 0];
    const result = Array(m + 1).fill(0);
    const visited = Array.from({ length: n }, () => Array(m).fill(0));

    function bfs(a, b) {
        let count = 0;
        visited[a][b] = 1;
        const q = [[a, b]];
        let min_y = b, max_y = b;

        while (q.length) {
            const [x, y] = q.shift();
            min_y = Math.min(min_y, y);
            max_y = Math.max(max_y, y);
            count++
            for (let i = 0; i < 4; i++) {
                const nx = x + dx[i];
                const ny = y + dy[i];
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (visited[nx][ny] === 0 && land[nx][ny] === 1) {
                    visited[nx][ny] = 1;
                    q.push([nx, ny]);
                }
            }
        }

        for (let i = min_y; i <= max_y; i++) result[i] += count;
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (visited[i][j] === 0 && land[i][j] === 1) bfs(i, j);
        }
    }

    return Math.max(...result);
}
