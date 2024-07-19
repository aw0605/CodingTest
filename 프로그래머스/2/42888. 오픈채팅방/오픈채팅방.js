function solution(record) {
    let answer = [];
    let user = {}
    
    for (let v of record){
        v = v.split(" ")
        if (v[0] !== "Leave") user[v[1]] = v[2]
    }
    
    for (let v of record){
        v = v.split(" ")
        if (v[0] === "Enter") answer.push(`${user[v[1]]}님이 들어왔습니다.`)
        else if (v[0] === "Leave") answer.push(`${user[v[1]]}님이 나갔습니다.`)
    }
    
    return answer;
}