function solution(a, b) {
    const day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
    let i = new Date(`2016-${a}-${b}`).getDay();
    return day[i];
}