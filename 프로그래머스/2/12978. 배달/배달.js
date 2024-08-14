function search(dist, arr) {
    const heap = [];
    heap.push([0, 1]);
    while (heap.length > 0) {
        heap.sort((a, b) => a[0] - b[0]);
        const [cost, node] = heap.shift();
        
        for (const [c, n] of arr[node]) {
            if (cost + c < dist[n]) {
                dist[n] = cost + c;
                heap.push([cost + c, n]);
            }
        }
    }
}

function solution(N, road, K) {
    const dist = Array(N + 1).fill(Infinity);
    dist[1] = 0;
    const arr = Array.from({ length: N + 1 }, () => []);

    for (const [u, v, w] of road) {
        arr[u].push([w, v]);
        arr[v].push([w, u]);
    }
    
    search(dist, arr);

    return dist.filter(d => d <= K).length;
}