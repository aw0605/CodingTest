function solution(lottos, win_nums) {
    const rank = [6,6,5,4,3,2,1]
    let curN = 0;
    let zeroN = 0
    
    for (let v of lottos){
        if (v === 0) zeroN++
        else if (win_nums.includes(v)) curN++
    }
    
    return [rank[curN+zeroN],rank[curN]];
}