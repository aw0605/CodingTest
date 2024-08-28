function changeTime(time) {
    time = time.split(":")
    return +time[0] * 60 + +time[1]
}

function solution(plans) {
  const answer = [];

  plans = plans
    .map(([name, start, playtime]) => [name, changeTime(start), +playtime])
    .sort((a, b) => b[1] - a[1]);

  while (plans.length) {
    const [name, start, playtime] = plans.pop();

    answer.forEach((v, i) => {
      if (start < v[1]) answer[i][1] += playtime;
    });
      
    answer.push([name, start + playtime]);
  }
    
  return answer.sort((a, b) => a[1] - b[1]).map(v => v[0]);
}