from lafmapi.artist import ArtistAPI

api_key = "your_api_key"
artist_api = ArtistAPI(api_key)

# Get information about an artist
artist_info = artist_api.get_info("Lil Uzi Vert")
print(artist_info["name"], artist_info["bio"]["summary"], artist_info["image"][2]["#text"])

# Get the top tracks for an artist
top_tracks = artist_api.get_top_tracks("SR")
for track in top_tracks:
    print(track["name"], track["playcount"], track["duration"])

# Get the top albums for an artist
top_albums = artist_api.get_top_albums("6ix9ine")
for album in top_albums:
    print(album["name"], album["playcount"], album["image"][2]["#text"])

# Search for artists
search_results = artist_api.search("West")
for result in search_results:
    print(result["name"], result["image"][2]["#text"], result["url"])

# Get similar artists for an artist
similar_artists = artist_api.get_similar_artists("Lil Mabu")
for artist in similar_artists:
    print(artist["name"], artist["image"][2]["#text"], artist["url"])
