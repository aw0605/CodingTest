function binarySearch(arr, target) {
    let left = 0, right = arr.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (arr[mid] >= target) right = mid - 1;
        else left = mid + 1;
    }

    return left;
}

function getInfos(info) {
    const infos = {};
    info.forEach(infoStr => {
        const arr = infoStr.split(" ");
        const score = parseInt(arr.pop());
        const key = arr.join(" ");
        if (infos[key]) infos[key].push(score);
        else infos[key] = [score];
    });

    for (const key in infos) infos[key].sort((a, b) => a - b);

    return infos;
}

function getResult (infos, query, score) {
  const infosKey = Object.keys(infos);
  return infosKey
    .filter(key => query.every(v => key.includes(v)))
    .reduce((a, key) => a + infos[key].length - binarySearch(infos[key], score), 0);
}

function solution(info, query) {
  let answer = [];
  const infos = getInfos(info)
  query
    .map(q => q.split(/ and | |-/i).filter(v => v !== ""))
    .forEach(q => {
      const score = q.pop();
      const result = getResult(infos, q, score);
      answer.push(result)
    })
    
  return answer;
}