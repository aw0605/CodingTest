function solution(age) {
    let alpha = 'abcdefghij';
    let ageArr = age.toString().split("")
    return ageArr.map(v => alpha[v]).join("");
}