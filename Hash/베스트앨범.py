from collections import defaultdict
from operator import itemgetter
def solution(genres, plays):
    answer = []

    # genre : total play
    total_plays_for_each_genre = defaultdict(int)
    # genre : [(num of play, idx1), ...]
    playlist_for_each_genre = defaultdict(list)

    for idx, num_of_play in enumerate(plays):
        genre = genres[idx]
        total_plays_for_each_genre[genre] += num_of_play
        playlist_for_each_genre[genre].append((num_of_play, idx))

    # list of pair (genre, total play)
    total_play_with_genres = total_plays_for_each_genre.items()

    # sort by total play
    for genre, total_play in sorted(total_play_with_genres, key=itemgetter(1), reverse=True):
        count = 0
        # sort by num of play
        for num_of_play, idx in sorted(playlist_for_each_genre[genre], key=itemgetter(0), reverse=True):
            if count >= 2: break
            answer.append(idx)
            count += 1

    return answer
