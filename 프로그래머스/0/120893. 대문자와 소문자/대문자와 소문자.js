function solution(my_string) {
    const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    const lower = "abcdefghijklmnopqrstuvwxyz"
    return [...my_string].map(v => upper.includes(v)? v.toLowerCase() : v.toUpperCase()).join("");
}