function solution(my_string) {
    return [...my_string].filter((v) => !isNaN(v)).map((v) => +v).sort((a,b) => a-b)
}