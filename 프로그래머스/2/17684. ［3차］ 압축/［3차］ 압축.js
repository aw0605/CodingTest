function solution(msg) {
    let answer = [];
    const dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split('').reduce((dict, v, i) => {
        dict[v] = i+1;
        return dict;
    }, {});
    dict["nextId"] = 27;
    
    for (let i = 0, j = 0; i < msg.length; i = j){
        j = msg.length;
        let longest = '';
        while (dict[(longest = msg.slice(i, j))] === undefined) --j;
        answer.push(dict[longest]);
        dict[longest + msg[j]] = dict["nextId"]++;
    }

    return answer;
}