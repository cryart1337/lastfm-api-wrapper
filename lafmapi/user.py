from .api import LastfmAPI
from .errors import LastfmAPIError


class UserAPI:
    def __init__(self, api_key):
        self.api = LastfmAPI(api_key)

    def get_info(self, username):
        """
        Get information about a specific Last.fm user, including their username,
        play count, and recent tracks.
        """
        params = {
            'method': 'user.getinfo',
            'user': username
        }
        try:
            response = self.api.get(params)
            user_info = response['user']
            return user_info
        except (KeyError, LastfmError):
            raise LastfmAPIError(f"Failed to get user info for {username}.")

    def get_top_artists(self, username):
        """
        Get the top artists for a specific Last.fm user, including their name,
        play count, and image.
        """
        params = {
            'method': 'user.gettopartists',
            'user': username
        }
        try:
            response = self.api.get(params)
            top_artists = response['topartists']['artist']
            return top_artists
        except (KeyError, LastfmError):
            raise LastfmAPIError(f"Failed to get top artists for {username}.")

    def get_recent_tracks(self, username):
        """
        Get the most recent tracks played by a specific Last.fm user, including
        the track name, artist name, and album name.
        """
        params = {
            'method': 'user.getrecenttracks',
            'user': username
        }
        try:
            response = self.api.get(params)
            recent_tracks = response['recenttracks']['track']
            return recent_tracks
        except (KeyError, LastfmError):
            raise LastfmAPIError(f"Failed to get recent tracks for {username}.")

    def get_top_tracks(self, username):
        """
        Get the top tracks played by a specific Last.fm user, including the track
        name, artist name, and play count.
        """
        params = {
            'method': 'user.gettoptracks',
            'user': username
        }
        try:
            response = self.api.get(params)
            top_tracks = response['toptracks']['track']
            return top_tracks
        except (KeyError, LastfmError):
            raise LastfmAPIError(f"Failed to get top tracks for {username}.")
