def solution(genres, plays):
    answer = []
    genre_dict = {}
    play_count = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genre_dict:
            genre_dict[genre] = []
            play_count[genre] = 0
        genre_dict[genre].append((i, play))
        play_count[genre] += play
        
    sort_genres = sorted(play_count.items(), key = lambda x: x[1], reverse = True)
    
    for genre, _ in sort_genres:
        sort_songs = sorted(genre_dict[genre], key = lambda x: (-x[1], x[0]))
        answer.extend([i for i,_ in sort_songs[:2]])
        
    return answer