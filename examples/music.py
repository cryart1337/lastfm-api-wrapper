from lafmapi.music import MusicAPI

api_key = "your_api_key"
music_api = MusicAPI(api_key)

# Search for a track
track = "Never Gonna Give You Up"
results = music_api.search_track(track)
for result in results:
    print(result["name"], result["artist"], result["album"], result["url"])

# Get information about a track
artist = "Rick Astley"
track_info = music_api.get_track_info(track, artist)
print(track_info["name"], track_info["duration"], track_info["listeners"], track_info["playcount"])
print(track_info["album"]["title"], track_info["album"]["image"][2]["#text"])
print(track_info["artist"]["name"], track_info["artist"]["image"][2]["#text"])

# Get lyrics for a track
lyrics = music_api.get_lyrics(track, artist)
print(lyrics)

