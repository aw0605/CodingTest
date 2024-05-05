function solution(my_string) {
    var answer = 0;
    return [...my_string].reduce((a,c) => !isNaN(c)? +a + +c : +a, 0);
}