from .api import LastfmAPI
from .errors import LastfmError


class LastfmUser:
    def __init__(self, api_key):
        self.api = LastfmAPI(api_key)

    def get_user_info(self, username):
        """
        Get information about a specific Last.fm user,
        including their username, play count, and recent tracks.
        """
        try:
            params = {
                "method": "user.getinfo",
                "user": username,
            }
            response = self.api.get(params)
            return response["user"]
        except LastfmError as e:
            print(f"Error occurred: {e}")
            return None

    def get_user_top_artists(self, username):
        """
        Get the top artists for a specific Last.fm user,
        including their name, play count, and image.
        """
        try:
            params = {
                "method": "user.gettopartists",
                "user": username,
            }
            response = self.api.get(params)
            return response["topartists"]["artist"]
        except LastfmError as e:
            print(f"Error occurred: {e}")
            return None

    def get_user_recent_tracks(self, username):
        """
        Get the most recent tracks played by a specific Last.fm user,
        including the track name, artist name, and album name.
        """
        try:
            params = {
                "method": "user.getrecenttracks",
                "user": username,
            }
            response = self.api.get(params)
            return response["recenttracks"]["track"]
        except LastfmError as e:
            print(f"Error occurred: {e}")
            return None

    def get_user_top_tracks(self, username):
        """
        Get the top tracks played by a specific Last.fm user,
        including the track name, artist name, and play count.
        """
        try:
            params = {
                "method": "user.gettoptracks",
                "user": username,
            }
            response = self.api.get(params)
            return response["toptracks"]["track"]
        except LastfmError as e:
            print(f"Error occurred: {e}")
            return None
