function solution(a, b) {
    const month = [31,29,31,30,31,30,31,31,30,31,30,31]
    const day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]

    let days = b
    for(let i = 0; i < a-1; i++){days += month[i];}

    return day[days%7];
}