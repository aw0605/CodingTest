function solution(players, callings) {
    let rank = {}
    players.map((v,i) => rank[v] = i)
    
    for (let call of callings){
        let curI = rank[call];
        let revI = curI - 1;

        rank[call] -= 1; 
        rank[players[revI]] += 1;

        players[curI] = players[revI];
        players[revI] = call;
    }
    return players;
}