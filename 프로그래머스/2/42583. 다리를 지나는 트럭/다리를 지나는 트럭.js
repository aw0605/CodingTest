function solution(bridge_length, weight, truck_weights) {
  let time = 0;
  const total = truck_weights.length;
  const end = [];
  let bridge = Array(bridge_length).fill(0);
  let curWeight = 0;

  for (let i = 0; truck_weights.length || end.length !== total; i++) {
    const leaveTruck = bridge.shift()
    if (leaveTruck) end.push(leaveTruck);
    curWeight -= leaveTruck;

    if (curWeight + truck_weights[0] <= weight) {
      const truck = truck_weights.shift()
      bridge.push(truck)
      curWeight += truck;
      time++;
    } else {
      bridge.push(0)
      time++;
    }

  }
    
  return time;
}
