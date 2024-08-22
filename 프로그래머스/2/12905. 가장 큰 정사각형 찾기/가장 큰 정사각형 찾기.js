function solution(board) {
    let side = 0;
    let n = board.length;
    let m = board[0].length;

    if (n <= 1 || m <= 1) return 1;

    for (let i = 1; i < n; i++) {
        for (let j = 1; j < m; j++) {
            if (board[i][j] >= 1){
                let min = Math.min(board[i-1][j], board[i-1][j-1], board[i][j-1]);
                board[i][j] = min+1;
                
                side = Math.max(side, min+1);
            }
        }
    }

    return side**2;
}