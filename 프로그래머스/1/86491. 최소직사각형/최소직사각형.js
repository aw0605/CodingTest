function solution(sizes) {
    let w = []
    let h = []
    for (let v of sizes){
        w.push(Math.max(...v))
        h.push(Math.min(...v))
    }
    return Math.max(...w) * Math.max(...h);
}