function solution(cap, n, deliveries, pickups) {
  let answer = 0;
  let [dIdx, pIdx] = [n - 1, n - 1];

  while (dIdx >= 0 || pIdx >= 0) {
    while (deliveries[dIdx] === 0 && dIdx >= 0) dIdx--
    while (pickups[pIdx] === 0 && pIdx >= 0) pIdx--
      
    let [dCap, pCap] = [cap, cap];
    answer += Math.max(dIdx + 1, pIdx + 1) * 2;
      
    while (dCap > 0 && dIdx >= 0) {
      if (deliveries[dIdx] > 0) {
        deliveries[dIdx]--
        dCap--
      } else dIdx--
    }
      
    while (pCap > 0 && pIdx >= 0) {
      if (pickups[pIdx] > 0) {
        pickups[pIdx]--
        pCap--
      } else pIdx--
    }
  }
    
  return answer;
}