function solution(strArr) {
    let lengthMap = {};
    
    strArr.forEach(v => {
        const length = v.length;
        if (!lengthMap[length]) lengthMap[length] = 1;
        else lengthMap[length]++;
    });
    
    let max = 0;
    for (const length in lengthMap) {
        if (lengthMap[length] > max) {
            max = lengthMap[length];
        }
    }
    
    return max;
}
