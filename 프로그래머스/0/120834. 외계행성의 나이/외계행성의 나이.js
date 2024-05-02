function solution(age) {
    let alpha = 'abcdefghijklmnopqrstuvwxyz';
    let ageArr = age.toString().split("")
    return ageArr.map(v => alpha[v]).join("");
}