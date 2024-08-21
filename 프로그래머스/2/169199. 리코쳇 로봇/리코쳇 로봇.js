function solution(board) {
        const [row, col] = [board.length, board[0].length];
        const dir = [[0, -1], [0, 1], [-1, 0], [1, 0]];
        const visited = new Set();
        let start = [0, 0];

        for (let i = 0; i < row; i++) {
          if(board[i].includes('R')) start = [i, board[i].indexOf('R')];
        }

        function bfs(start) {
          const q = [[...start, 0]];

          while (q.length) {
            const [x, y, cnt] = q.shift();

            for (let i = 0; i < dir.length; i++) {
              let [nx, ny] = [x + dir[i][0], y + dir[i][1]];
              if (nx < 0 || nx >= row || ny < 0 || ny >= col || board[nx][ny] === 'D') continue;

              switch (i) {
                case 0: // left
                  while (ny >= 0 && board[nx][ny] !== 'D') ny--;
                  ny++;
                  break;
                case 1: // right
                  while (ny < col && board[nx][ny] !== 'D') ny++;
                  ny--;
                  break;
                case 2: // top
                  while (nx >= 0 && board[nx][ny] !== 'D') nx--;
                  nx++;
                  break;
                case 3: // bottom
                  while (nx < row && board[nx][ny] !== 'D') nx++;
                  nx--;
                  break;
              }
              if (board[nx][ny] === 'G') return cnt + 1;

              let r1 = `${x}${y}${nx}${ny}`;
              let r2 = `${nx}${ny}${x}${y}`;
              if (!visited.has(r1) && !visited.has(r2)) {
                visited.add(r1);
                visited.add(r2);
                q.push([nx, ny, cnt + 1]);
              }
            }
          }
        }

        return bfs(start) ?? -1;
      }