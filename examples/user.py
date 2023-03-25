from lafmapi.user import UserAPI

api_key = "your_api_key"
user_api = UserAPI(api_key)

# Get information about a user
user_info = user_api.get_info("Csmn__")
print(user_info["name"], user_info["country"], user_info["playcount"])

# Get a user's top tracks
top_tracks = user_api.get_top_tracks("Csmn__")
for track in top_tracks:
    print(track["name"], track["artist"]["name"], track["playcount"])

# Get a user's top artists
top_artists = user_api.get_top_artists("Csmn__")
for artist in top_artists:
    print(artist["name"], artist["playcount"])

# Get a user's recent tracks
recent_tracks = user_api.get_recent_tracks("Csmn__")
for track in recent_tracks:
    print(track["name"], track["artist"]["name"], track["date"]["#text"])

# Get a user's loved tracks
loved_tracks = user_api.get_loved_tracks("Csmn__")
for track in loved_tracks:
    print(track["name"], track["artist"]["name"])
