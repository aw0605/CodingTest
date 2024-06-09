function solution(players, callings) {
    let rank = {}
    players.map((v,i) => rank[v] = i)
    
    for (let i = 0; i < callings.length; i++){
        const curRank = rank[callings[i]];
        const revPlayer = players[curRank-1];
      
        players[curRank-1] = callings[i];
        players[curRank] = revPlayer;
      
        rank[callings[i]] = curRank - 1;
        rank[revPlayer] = curRank;
    }
    return players;
}