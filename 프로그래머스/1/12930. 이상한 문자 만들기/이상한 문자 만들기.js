function solution(s) {
    return s.split(" ").map((v) => ([...v].map((x,i) => i % 2? x.toLowerCase() : x.toUpperCase())).join("")).join(" ");
}