function solution(keyinput, board) {
    let x = 0, y = 0;
    for(let key of keyinput){
        if (key === "left" && x > -Math.trunc(board[0]/2)){
            x -= 1
        } else if (key === "right" && x < Math.trunc(board[0]/2)){
            x += 1
        } else if (key === "up" && y < Math.trunc(board[1]/2)){
            y += 1
        } else if(key === "down" && y > -Math.trunc(board[1]/2)){
            y -= 1
        }
    }
    
    return [x,y];
}