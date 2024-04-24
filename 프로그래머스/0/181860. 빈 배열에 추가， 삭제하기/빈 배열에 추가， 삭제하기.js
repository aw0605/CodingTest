function solution(arr, flag) {
  return arr.reduce(
    (prev, v, i) => (flag[i] ? [...prev, ...new Array(v * 2).fill(v)] : prev.slice(0, -v)),
    [],
  );
}