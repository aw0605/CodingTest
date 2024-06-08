function solution(today, terms, privacies) {
  const answer = [];
  const term = {};
  const tDate = new Date(today);
    
  terms.map(v => {
    const [type, n] = v.split(" ");
    term[type] = +n;
  });

  privacies.forEach((v, i) => {
    const [date, type] = v.split(" ");

    const pDate = new Date(date);
    pDate.setMonth(pDate.getMonth() + term[type]);

    if (tDate >= pDate) answer.push(i + 1);
  });

  return answer;
}