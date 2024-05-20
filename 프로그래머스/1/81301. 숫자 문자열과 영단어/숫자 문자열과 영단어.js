function solution(s) {
    const enNum = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let answer = s;

    for(let i = 0; i < enNum.length; i++) {
        let arr = answer.split(enNum[i]);
        answer = arr.join(i);
    }

    return Number(answer);
}