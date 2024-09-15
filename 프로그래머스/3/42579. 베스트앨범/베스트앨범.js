function solution(genres, plays) {
    let answer = [];
    const g_dict = {}, p_dict = {}
    
    for (let i = 0; i < genres.length; i++){
        genre = genres[i]
        play = plays[i]
        if (!g_dict[genre]) {
            g_dict[genre] = []
            p_dict[genre] = 0
        }
        g_dict[genre].push([i, play])
        p_dict[genre] += play
    }
    
    let sortGenres = Object.entries(p_dict).sort((a, b) => b[1] - a[1]);

    for (let [genre, _] of sortGenres) {
        let sortedSongs = g_dict[genre].sort((a, b) => {
            if (b[1] === a[1]) return a[0] - b[0];
            else return b[1] - a[1];
        });
        answer.push(...sortedSongs.slice(0, 2).map(song => song[0]));
    }
    
    return answer;
}