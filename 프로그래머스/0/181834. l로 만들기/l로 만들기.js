function solution(myString) {
    const replaceI = "abcdefghijk"
    return [...myString].map(v => replaceI.includes(v)? v = "l" : v).join("")
}