function solution(keymap, targets) {
    let answer = [];
    const map = {}
    for (let key of keymap) {
        key.split("").map((v, i) => map[v] = (map[v] < i+1 ? map[v] : i+1))
    }
    
    for (let target of targets) {
        answer.push(target.split("").reduce((a, c) => a += map[c], 0) || -1)
    }
    return answer;
}