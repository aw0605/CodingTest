function solution(babbling) {
    let answer = 0;
    const words = ["aya", "ye", "woo", "ma"];
    
    for (let v of babbling) {
        for (let w of words) {
            if (v.includes(w.repeat(2))) break;
            v = v.split(w).join(" ");
        }
        if (v.split(" ").join("") === "") answer++
    }
    return answer;
}