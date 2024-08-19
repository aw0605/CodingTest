function solution(maps) {
  let start = [];
  let lever = [];
  let exit = [];
  const table = maps.map((r) => r.split(""));
  const rLen = table.length;
  const cLen = table[0].length;

  table.forEach((row, x) => {
    row.forEach((cel, y) => {
      if (cel === "S") start = [x, y];
      else if (cel === "L") lever = [x, y];
      else if (cel == "E") exit = [x, y];
    });
  });

  const move = ([x1, y1], [x2, y2]) => {
    const dp = new Array(rLen).fill(null).map(() => new Array(cLen).fill(Infinity));
    const visited = new Array(rLen).fill(null).map(() => new Array(cLen).fill(false));

    dp[x1][y1] = 0;
    const queue = [[x1, y1]];

    while (queue.length) {
      const [px, py] = queue.shift();
      if (visited[px][py]) continue;
      visited[px][py] = true;
      const nexts = [
        [px - 1, py],
        [px + 1, py],
        [px, py - 1],
        [px, py + 1],
      ];
        
      for (const [nx, ny] of nexts) {
        if (nx < 0 || nx >= rLen || ny < 0 || ny >= cLen || table[nx][ny] === "X") continue;
        dp[nx][ny] = Math.min(dp[nx][ny], dp[px][py] + 1);
        if (visited[nx][ny]) continue;
        queue.push([nx, ny, dp[nx][ny]]);
      }
    }
    return dp[x2][y2] === Infinity ? -1 : dp[x2][y2];
  };
    
  const first = move(start, lever);
  const second = move(lever, exit);

  return (first === -1 || second === -1) ? -1 : first + second;
}