function solution(info, edges) {
    let answer = 0;
    const q = [[0, 1, 0, new Set()]];

    function buildTree(info, edges) {
        const tree = Array.from({ length: info.length }, () => []);
        for (let edge of edges) tree[edge[0]].push(edge[1]);
        return tree;
    }
    const tree = buildTree(info, edges);

    while (q.length) {
        const [cur, sheep, wolf, visited] = q.shift();
        answer = Math.max(answer, sheep);
        const newVisited = new Set(visited);
        tree[cur].forEach(node => newVisited.add(node));
        
        newVisited.forEach(nNode => {
            if (info[nNode]) {
                if (sheep !== wolf + 1) {
                    const nextVisited = new Set(newVisited);
                    nextVisited.delete(nNode);
                    q.push([nNode, sheep, wolf + 1, nextVisited]);
                }
            } else {
                const nextVisited = new Set(newVisited);
                nextVisited.delete(nNode);
                q.push([nNode, sheep + 1, wolf, nextVisited]);
            }
        });
    }

    return answer;
}
