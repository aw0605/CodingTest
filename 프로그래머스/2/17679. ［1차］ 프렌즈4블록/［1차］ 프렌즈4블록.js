function solution(m, n, board) {
  let answer = 0;
  board = board.map(v => v.split(''));
  let tmp = new Set();

  while (true) {
    for (let i = 0; i < m - 1; i++) {
      for (let j = 0; j < n - 1; j++) {
        let c = board[i][j];
        if (c === '') continue;

        if (
          board[i][j + 1] === c &&
          board[i + 1][j] === c &&
          board[i + 1][j + 1] === c
        ) {
          tmp.add(`${i},${j}`);
          tmp.add(`${i},${j + 1}`);
          tmp.add(`${i + 1},${j}`);
          tmp.add(`${i + 1},${j + 1}`);
        }
      }
    }

    if (tmp.size) {
      answer += tmp.size;
      tmp.forEach(position => {
        const [i, j] = position.split(',').map(Number);
        board[i][j] = '';
      });
      tmp.clear();
    } else break;

    while (true) {
      let moved = false;
      for (let i = m - 2; i >= 0; i--) {
        for (let j = 0; j < n; j++) {
          if (board[i][j] !== '' && board[i + 1][j] === '') {
            board[i + 1][j] = board[i][j];
            board[i][j] = '';
            moved = true;
          }
        }
      }
      if (!moved) break;
    }
  }

  return answer;
}
     
