function solution(n) {
    let i = n + 1
    let nCount = ([...n.toString(2)]).filter(v => v === "1").length
    
    while (true) {
        if (nCount === ([...i.toString(2)]).filter(v => v === "1").length) return i
        i++
    }
}