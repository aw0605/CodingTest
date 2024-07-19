function solution(record) {
    const user = {};
    const answer = [];
    const status = {
        'Enter': '님이 들어왔습니다.',
        'Leave': '님이 나갔습니다.'
    }

    record.forEach((v) => {
        const [s, id, nick] = v.split(' ');

        if (s !== "Change") answer.push([s, id]);
        if (nick) user[id] = nick;
    })

    return answer.map(([s, id]) => {
        return `${user[id]}${status[s]}`;    
    })
}