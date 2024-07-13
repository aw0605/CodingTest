function solution(dirs) {
    let moves = {L: [-1, 0], R: [1, 0], U: [0, 1], D: [0, -1]};
    let s = [0, 0];
    let route = new Set();
    
    for (let dir of dirs) {
        let nx = s[0] + moves[dir][0];
        let ny = s[1] + moves[dir][1];
        
        if (nx > 5 || nx < -5 || ny > 5 || ny < -5) continue;
        
        route.add("" + s[0] + s[1] + nx + ny);
        route.add("" + nx + ny + s[0] + s[1]);
        
        s = [nx, ny];
    }
    
    return route.size / 2;
}