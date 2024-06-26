function solution(s) {
    let dict = {}
    for (let v of s.match(/\d+/g)) dict[v] = (dict[v] || 0) + 1;
    
    return Object.keys(dict).map(v => +v).sort((a, b) => dict[b] - dict[a]);
}