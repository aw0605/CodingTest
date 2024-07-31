function solution(n) {
  let tri = Array(n).fill().map((_, i) => Array(i + 1).fill())
  let x = -1, y = 0
  let num = 0
  
  for (let i = n; i > 0; i -= 3) {
    tri[++x][y] = ++num
    for (let j = 0; j < i - 1; j++) tri[++x][y] = ++num
    for (let j = 0; j < i - 1; j++) tri[x][++y] = ++num
    for (let j = 0; j < i - 2; j++) tri[--x][--y] = ++num
  }
  return tri.flat()
}