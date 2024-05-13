function solution(i, j, k) {
    let result = ""
    for (let s = i; s <= j; s++){
        result += s
    }
    return [...result].filter(v => v === String(k)).length;
}