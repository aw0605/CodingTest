function solution(babbling) {
    let possible = 0
    const pronunciation = ["aya", "ye", "woo", "ma"]
    for (let w of babbling){
        for (let v of pronunciation){
            w = w.replace(v, "1")
        }
        if (w.replace(/1/g, "") === "") possible++
    }
    return possible;
}