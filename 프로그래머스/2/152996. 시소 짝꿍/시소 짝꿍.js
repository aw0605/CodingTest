function solution(weights) {
  weights.sort((a, b) => b - a);
  const dict = {};

  return weights.reduce((answer, w) => {
    if (dict[w]) answer += dict[w];
    if (dict[(w * 4) / 3]) answer += dict[(w * 4) / 3];
    if (dict[(w * 3) / 2]) answer += dict[(w * 3) / 2];
    if (dict[w * 2]) answer += dict[w * 2];

    dict[w] = (dict[w] || 0) + 1;
    return answer;
  }, 0);
}