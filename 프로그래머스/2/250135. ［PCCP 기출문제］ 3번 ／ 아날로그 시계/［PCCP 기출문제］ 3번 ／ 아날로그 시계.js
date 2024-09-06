function solution(h1, m1, s1, h2, m2, s2) {
    const getCount = (h, m, s) => {
    let [mCount, hCount] = [0, 0];
    let result = 0;
    mCount += h * 59 + m;
    hCount += h * 60 + m;
    result--

    const curMDegree = m * 6;
    const curHDegree = 30 * (h % 12) + 0.5 * m;
    const condition1 = curMDegree <= 5.9 * s;
    const condition2 = curHDegree <= (6 - 1 / 120) * s;

    if (condition1) mCount++
    if (condition2) hCount++

    if (h >= 12) {
      hCount--
      result--
    }

    result += mCount + hCount - 1;

    return result;
  };

  let result = getCount(h2, m2, s2) - getCount(h1, m1, s1);
  if (s1 === 0 && m1 === 0) result++

  return result;
}