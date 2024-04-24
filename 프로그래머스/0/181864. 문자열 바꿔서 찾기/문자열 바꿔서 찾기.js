function solution(myString, pat) {
    let newString = [...myString].map(v => v === "A"? "B" : "A").join("");
    return newString.includes(pat)? 1 : 0;
}