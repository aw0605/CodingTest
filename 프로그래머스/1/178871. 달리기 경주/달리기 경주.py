def solution(players, callings):
    rank = {v:i for i,v in enumerate(players)}
    
    for call in callings:
        curRank = rank[call]
        
        rank[call] -= 1
        rank[players[curRank-1]] += 1
        
        players[curRank-1], players[curRank] = call, players[curRank-1]
        
    return players