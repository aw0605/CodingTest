function solution(elements) {
    const sum = (arr) => arr.reduce((a, c) => a + c, 0);
    
    let comb = new Set();
    const element = elements.concat(elements);
    
    for (let i = 0; i < elements.length; i++){
        for (let j = 0; j < elements.length; j++){
            comb.add(sum(element.slice(i, i+j+1)))
        }
    }
    
    return comb.size;
}