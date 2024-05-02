function solution(rsp) {
    return [...rsp].map(v => {
        return v === "2"? "0" : v === "0"? "5" : "2"
    }).join("");
}