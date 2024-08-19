function BFS(start, arr, target){
  let time = 0;
  const dx  = [-1,1,0,0];
  const dy = [0,0,-1,1];
  arr[start[0]][start[1]] = "X";
  let queue = [start];

  while (queue.length > 0){
    let size = queue.length;
    for (let i = 0; i < size; i++){
      let [x,y] = queue.shift();
      for (var k = 0; k < 4; k++){
        let nx = x + dx[k];
        let ny = y + dy[k];
        if(nx>=0 && ny>=0 && nx<arr.length && ny<arr[0].length && arr[nx][ny]!=="X"){
          if (target === arr[nx][ny]) return time+1;

          queue.push([nx,ny]);
          arr[nx][ny] = 'X';
        }
      }
    }
    time++;
  }

  return -1;
}

function solution(maps) {
  let lCord;
  let sCord;
  let maps1 = maps.map((v) => v.split(""));
  let maps2 = maps.map((v) => v.split(""));
    
  for (var x = 0; x < maps.length; x++){
    for (var y = 0; y < maps[0].length; y++){
      if (maps[x][y] === "L") lCord = [x,y];
      if(maps[x][y] === "S") sCord = [x,y];
    }
  }

  let a = BFS(sCord, [...maps1], "L");
  let b = BFS(lCord, [...maps2], "E")

  return (a === -1 || b === -1) ? -1 : a+b;
}