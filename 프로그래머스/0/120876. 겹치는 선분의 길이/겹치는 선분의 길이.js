function solution(lines) {
    let min = Math.min(...lines.flat());
    let max = Math.max(...lines.flat());
    let numArr = Array(max-min+1).fill(0);

    for (let line of lines) {
        if (min < 0) {
            line[0] -= min
            line[1] -= min
        }
        for (let i = line[0]; i < line[1]; i++) numArr[i]++;
    }

    return numArr.filter(v => v > 1).length;
}