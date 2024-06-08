function solution(today, terms, privacies) {
  let answer = [];
  let [y, m, d] = today.split(".").map(Number);
  const tdates = y * 12 * 28 + m * 28 + d;
  let term = {};

  terms.map(v => {
    let [type, n] = v.split(" ");
    term[type] = +n;
  });
    
  privacies.map((v, i) => {
    let [date, type] = v.split(" ");
    date = date.split(".").map(Number);
    let dates = date[0] * 12 * 28 + date[1] * 28 + date[2] + term[type] * 28;
    if (dates <= tdates) answer.push(i + 1);
  });
  return answer;
}