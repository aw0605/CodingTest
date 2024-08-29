function getCount(board, kind) {
  return board.reduce((a, r) => {
    return a + r.split("").filter((v) => v === kind).length;
  }, 0);
}

function checkWin(board, kind) {
  const winLines = [
    [board[0][0], board[0][1], board[0][2]],
    [board[1][0], board[1][1], board[1][2]],
    [board[2][0], board[2][1], board[2][2]],
    [board[0][0], board[1][0], board[2][0]],
    [board[0][1], board[1][1], board[2][1]],
    [board[0][2], board[1][2], board[2][2]],
    [board[0][0], board[1][1], board[2][2]],
    [board[0][2], board[1][1], board[2][0]],
  ];

  return winLines.some((line) => line.every((v) => v === kind));
}

function isBoardValid(board) {
  const oCount = getCount(board, "O");
  const xCount = getCount(board, "X");

  if (xCount > oCount || oCount > xCount + 1) return false;
  if (checkWin(board, "O") && oCount !== xCount + 1) return false;
  if (checkWin(board, "X") && xCount !== oCount) return false;

  return true;
}

function solution(board) {
  if (isBoardValid(board)) return 1;
  else return 0;
}