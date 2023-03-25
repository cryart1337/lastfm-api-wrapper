from lafmapi.api import LastfmAPI

# create LastfmAPI instance with your own API key
api_key = "your_api_key"
lastfm_api = LastfmAPI(api_key)

# get info about an artist
artist_name = "Playboi Carti"
artist_info = lastfm_api.get_artist_info(artist_name)
print(artist_info["name"])
print(artist_info["stats"]["listeners"])

# get top tracks for an artist
artist_name = "Lil Nax X"
top_tracks = lastfm_api.get_top_tracks(artist_name)
for track in top_tracks:
    print(track["name"], "-", track["playcount"])

# get top albums for an artist
artist_name = "Lil Pump"
top_albums = lastfm_api.get_top_albums(artist_name)
for album in top_albums:
    print(album["name"], "-", album["playcount"])

# search for an artist
query = "Obsessed with You"
search_results = lastfm_api.search_artists(query)
for result in search_results:
    print(result["name"], "-", result["listeners"])

# get similar artists
artist_name = "Central Cee"
similar_artists = lastfm_api.get_similar_artists(artist_name)
for artist in similar_artists:
    print(artist["name"], "-", artist["match"])

# get info about a track
track_name = "Starlight"
artist_name = "Dave"
track_info = lastfm_api.get_track_info(track_name, artist_name)
print(track_info["name"])
print(track_info["artist"]["name"])

# get info about a user
username = "Csmn__"
user_info = lastfm_api.get_user_info(username)
print(user_info["name"])
print(user_info["playcount"])

# get user's top artists
username = "Csmn__"
top_artists = lastfm_api.get_user_top_artists(username)
for artist in top_artists:
    print(artist["name"], "-", artist["playcount"])

# get user's recently played tracks
username = "Csmn__"
recent_tracks = lastfm_api.get_user_recent_tracks(username)
for track in recent_tracks:
    print(track["name"], "-", track["artist"]["#text"])

# get user's top tracks
username = "Csmn__"
top_tracks = lastfm_api.get_user_top_tracks(username)
for track in top_tracks:
    print(track["name"], "-", track["playcount"])
