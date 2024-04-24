function solution(binomial) {
    let [a, op, b] = binomial.split(" ");
    a = +a;
    b = +b;
    switch(op){
        case "+": return a + b;
        case "-": return a - b;
        case "*": return a * b;
    }
}