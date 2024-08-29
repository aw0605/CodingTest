function solution(cards) {
    cards = cards.map(v => v - 1)

    let group = cards.map((v,i) => { 
        let save = 0
        return Array.from(new Set(cards.map(a => {
            save = cards[v]
            v = save
            return save
        }))).length
    })

    const result = Array.from(new Set(group.sort((a,b) => b - a)))
    if (result[0] === cards.length) return 0
    else if (result.length === 1) return result[0] * result[0]
    else return result[0] * result[1]
}