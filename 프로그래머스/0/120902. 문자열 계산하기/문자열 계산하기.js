function solution(my_string) {
    const stack = [];
    let sign = 1;
    
    for (const v of my_string.split(" ")) {
        if (v === "+") {
            sign = 1;
        } else if (v === "-") {
            sign = -1;
        } else {
            stack.push(v * sign);
        }
    }

    return stack.reduce((a,b) => a + b, 0);
}