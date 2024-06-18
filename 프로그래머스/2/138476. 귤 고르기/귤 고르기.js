function solution(k, tangerine) {
  let answer = 0;
  const tang_dict = {};
    
  tangerine.forEach((v) => tang_dict[v] = (tang_dict[v] || 0) + 1);
  const tangArr = Object.values(tang_dict).sort((a, b) => b - a);
    
  for (const v of tangArr) {
      k -= v;
      answer++;
      if (k <= 0) break;
  }
    
  return answer;
}