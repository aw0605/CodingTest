function solution(n) {
  const answer = [];
    
  const hanoiTop = (n, s, e, by) => {
    if (n === 1) {
      answer.push([s, e]);
      return;
    }
      
    hanoiTop(n - 1, s, by, e);
    answer.push([s, e]);
    hanoiTop(n - 1, by, e, s);
  }
  
  hanoiTop(n, 1, 3, 2);
    
  return answer;
}