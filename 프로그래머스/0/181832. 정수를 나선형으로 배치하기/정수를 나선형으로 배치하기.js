function solution(n) {
    let answer = new Array(n).fill(null).map(() => new Array(n).fill(0));
    
    let dx = [0, 1, 0, -1];
    let dy = [1, 0, -1, 0];
    let direction = 0;
    let x = 0, y = 0; 
    
    for (let num = 1; num <= n ** 2; num++) {
        answer[x][y] = num;
        
        let nx = x + dx[direction];
        let ny = y + dy[direction];
        
        if (0 <= nx && nx < n && 0 <= ny && ny < n && answer[nx][ny] === 0){           x = nx;
            y = ny;
        } else {
            direction = (direction + 1) % 4;
            x += dx[direction];
            y += dy[direction];
        }
    }
    
    return answer;
}
