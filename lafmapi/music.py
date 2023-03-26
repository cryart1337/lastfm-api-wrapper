from .api import LastfmAPI
from .errors import LastfmAPIError


class MusicAPI:
    def __init__(self, api_key):
        self.api = LastfmAPI(api_key)

    def search_track(self, track_name):
        """
        Search for tracks that match a given query, returning their name, artist,
        album, and Last.fm URL.
        """
        params = {
            'method': 'track.search',
            'track': track_name
        }
        try:
            response = self.api.get(params)
            search_results = response['results']['trackmatches']['track']
            return search_results
        except (KeyError, LastfmError):
            raise LastfmAPIError(f"No results found for {track_name}.")

    def get_track_info(self, track_name, artist_name):
        """
        Get information about a specific track, including its name, duration,
        play count, artist name, album name, album icon, artist icon, song icon,
        listeners, Scrobbles, tags, similar tracks, and play links.
        """
        params = {
            'method': 'track.getInfo',
            'track': track_name,
            'artist': artist_name
        }
        try:
            response = self.api.get(params)
            track_info = response['track']
            return track_info
        except (KeyError, LastfmError):
            raise LastfmAPIError(f"Failed to get track info for {track_name} by {artist_name}.")

    def get_lyrics(self, track_name, artist_name):
        """
        Get the lyrics for a specific song.
        """
        params = {
            'method': 'track.getLyrics',
            'track': track_name,
            'artist': artist_name
        }
        try:
            response = self.api.get(params)
            lyrics = response['lyrics']['lyrics_body']
            return lyrics
        except (KeyError, LastfmError):
            raise LastfmAPIError(f"No lyrics found for {track_name} by {artist_name}.")
