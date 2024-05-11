function solution(spell, dic) {
    let answer = []
    for (let v of dic){
        let result = 0;
        for (let i of spell){
            if(v.includes(i)) result++
        }
        if(result === spell.length) answer.push(v)
    }

    return answer.length > 0? 1 : 2;
}