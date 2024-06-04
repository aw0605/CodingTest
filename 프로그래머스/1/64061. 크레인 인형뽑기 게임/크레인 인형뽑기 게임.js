function solution(board, moves) {
    let answer = 0;
    let dolls = [];
    
    for (let j of moves){
        for (let i = 0; i < board.length; i++){
            let doll = board[i][j-1]
            if (doll !== 0){
                if (dolls && dolls[dolls.length-1] === doll){
                    dolls.pop();
                    answer += 2
                }
                else {dolls.push(doll)}
                board[i][j-1] = 0
                break
            }
        }
    }
    
    return answer;
}