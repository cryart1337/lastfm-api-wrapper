import requests
from .errors import LastfmAPIError

class LastfmAPI:
    API_BASE_URL = "http://ws.audioscrobbler.com/2.0/"
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def _make_request(self, method, params):
        params["api_key"] = self.api_key
        params["format"] = "json"
        response = requests.get(self.API_BASE_URL + "?method=" + method, params=params)
        response_data = response.json()
        if "error" in response_data:
            raise LastfmAPIError(response_data["message"])
        return response_data
    
    def get_artist_info(self, artist_name):
        params = {"artist": artist_name}
        response_data = self._make_request("artist.getinfo", params)["artist"]
        return response_data
    
    def get_top_tracks(self, artist_name):
        params = {"artist": artist_name}
        response_data = self._make_request("artist.gettoptracks", params)["toptracks"]["track"]
        return response_data
    
    def get_top_albums(self, artist_name):
        params = {"artist": artist_name}
        response_data = self._make_request("artist.gettopalbums", params)["topalbums"]["album"]
        return response_data
    
    def search_artists(self, query):
        params = {"artist": query}
        response_data = self._make_request("artist.search", params)["results"]["artistmatches"]["artist"]
        return response_data
    
    def get_similar_artists(self, artist_name):
        params = {"artist": artist_name}
        response_data = self._make_request("artist.getsimilar", params)["similarartists"]["artist"]
        return response_data
    
    def get_track_info(self, track_name, artist_name):
        params = {"track": track_name, "artist": artist_name}
        response_data = self._make_request("track.getinfo", params)["track"]
        return response_data
    
    def get_user_info(self, username):
        params = {"user": username}
        response_data = self._make_request("user.getinfo", params)["user"]
        return response_data
    
    def get_user_top_artists(self, username):
        params = {"user": username}
        response_data = self._make_request("user.gettopartists", params)["topartists"]["artist"]
        return response_data
    
    def get_user_recent_tracks(self, username):
        params = {"user": username, "limit": 10}
        response_data = self._make_request("user.getrecenttracks", params)["recenttracks"]["track"]
        return response_data
    
    def get_user_top_tracks(self, username):
        params = {"user": username}
        response_data = self._make_request("user.gettoptracks", params)["toptracks"]["track"]
        return response_data
