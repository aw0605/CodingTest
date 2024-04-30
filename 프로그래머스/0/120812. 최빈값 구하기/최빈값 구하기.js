function solution(array) {
    let answerArr = new Array(Math.max(...array)+1).fill(0);
    
    for (let i = 0; i < array.length; i++) {
        answerArr[array[i]] += 1;
    }
    
    let mode = Math.max(...answerArr)
    
    if (answerArr.indexOf(mode) !== answerArr.lastIndexOf(mode)) {
        return -1
    } else {
        return answerArr.indexOf(mode);
    };
}