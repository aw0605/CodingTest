function solution(numbers) {
    const alphaArr = ["zero", "one", "two", "three", "four", "five",'six', "seven", "eight", "nine"]
    alphaArr.forEach((v,i) => numbers = numbers.replaceAll(v, i));
    return +numbers;
}