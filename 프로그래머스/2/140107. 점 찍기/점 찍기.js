function solution(k, d) {
  let answer = 0;
    
  for (let x = 0; x <= d; x += k) {
      answer += Math.ceil(Math.sqrt(d*d - x*x)/k) + (Math.sqrt(d*d - x*x) % k === 0 ? 1 : 0)
  }
    
  return answer;
}