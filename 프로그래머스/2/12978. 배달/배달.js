const solution = (N, road, K) => {
  const graph = [...Array(N + 1)].map((m) => []);
  road.forEach((r) => {
    graph[r[0]].push([r[1], r[2]]);
    graph[r[1]].push([r[0], r[2]]);
  });

  const weight = new Array(graph.length).fill(Infinity);

  const dfs = function (start, w) {
    if (weight[start] < w) {
      return;
    } else {
      weight[start] = w;
      for (let item of graph[start]) {
        const [a, b] = item;
        dfs(a, w + b);
      }
    }
  };

  dfs(1, 0);

  return weight.filter((w) => w <= K).length;
};
