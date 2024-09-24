function find(parent, i) {
    if (parent[i] === i) return i;
    parent[i] = find(parent, parent[i]);
    return parent[i];
}

function union(parent, rank, x, y) {
    let xroot = find(parent, x);
    let yroot = find(parent, y);

    if (rank[xroot] < rank[yroot]) parent[xroot] = yroot;
    else if (rank[xroot] > rank[yroot]) parent[yroot] = xroot;
    else {
        parent[yroot] = xroot;
        rank[xroot]++;
    }
}

function solution(n, costs) {
    costs.sort((a, b) => a[2] - b[2]);
    let parent = Array.from({ length: n }, (_, i) => i);
    let rank = Array(n).fill(0);
    let cost = 0;
    let edges = 0;

    for (let edge of costs) {
        if (edges === n - 1) break;
        let [u, v, weight] = edge;
        let x = find(parent, u);
        let y = find(parent, v);

        if (x !== y) {
            union(parent, rank, x, y);
            cost += weight;
            edges++;
        }
    }

    return cost;
}
