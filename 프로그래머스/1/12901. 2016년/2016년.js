function solution(a, b) {
    const day = ['THU','FRI','SAT','SUN','MON','TUE','WED'];
    const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    let daySum;
    if(a == 1) daySum = b;
    else daySum = month.slice(0, a - 1).reduce((a,c) => a + c) + b;
    return day[daySum%7];
}