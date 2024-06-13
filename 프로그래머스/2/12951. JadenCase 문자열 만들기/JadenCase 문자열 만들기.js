function solution(s) {
    return s.toLowerCase().split(" ").map(v => {
        return v? (isNaN(v[0])? v[0].toUpperCase() + v.slice(1) : v) : "";
    }).join(" ")
}