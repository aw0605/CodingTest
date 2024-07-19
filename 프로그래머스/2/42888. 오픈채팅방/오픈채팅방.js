function solution(record) {
    let answer = []
    const user = new Map()

    record.forEach(v => {
        let [s, uid, nick] = v.split(' ')
        if (s === 'Enter' || s === 'Change') user.set(uid, nick)
    })

    record.forEach(v => {
        let [s, uid] = v.split(' ')
        if (s === 'Enter') answer.push(`${user.get(uid)}님이 들어왔습니다.`)
        if (s === 'Leave') answer.push(`${user.get(uid)}님이 나갔습니다.`)
    })

    return answer
}