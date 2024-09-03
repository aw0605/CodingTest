function solution(line) {
  const points = [];

  for (let i = 0; i < line.length; i++) {
    for (let j = i + 1; j < line.length; j++) {
      const [a, b, e] = line[i];
      const [c, d, f] = line[j];
      const adbc = a * d - b * c;
        
      if (((b * f - e * d) / adbc) % 1 === 0 &&((e * c - a * f) / adbc) % 1 === 0) {
        points.push([(b * f - e * d) / adbc, (e * c - a * f) / adbc]);
      }
    }
  }

  let minX = Infinity, minY = Infinity, maxY = -Infinity, maxX = -Infinity;

  for (let [x, y] of points) {
    minX = Math.min(minX, x);
    maxX = Math.max(maxX, x);
    minY = Math.min(minY, y);
    maxY = Math.max(maxY, y);
  }

  const width = maxX - minX + 1;
  const height = maxY - minY + 1;

  const star = Array.from(Array(height), () => Array(width).fill("."));

  for (let [x, y] of points) star[maxY - y][x - minX] = "*";

  return star.map((a) => a.join(""));
}