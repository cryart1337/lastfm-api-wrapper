from .api import LastfmAPI
from .errors import LastfmAPIError


class ArtistAPI:
    def __init__(self, api_key):
        self.api = LastfmAPI(api_key)

    def get_info(self, artist_name):
        """
        Get information about a specific artist, including their name, biography,
        images, and similar artists.
        """
        params = {
            'method': 'artist.getinfo',
            'artist': artist_name
        }
        try:
            response = self.api.get(params)
            artist_info = response['artist']
            return artist_info
        except (KeyError, LastfmError):
            raise LastfmAPIError(f"Failed to get artist info for {artist_name}.")

    def get_top_tracks(self, artist_name):
        """
        Get the top tracks for a specific artist, including their name, play count,
        and duration.
        """
        params = {
            'method': 'artist.gettoptracks',
            'artist': artist_name
        }
        try:
            response = self.api.get(params)
            top_tracks = response['toptracks']['track']
            return top_tracks
        except (KeyError, LastfmError):
            raise LastfmAPIError(f"Failed to get top tracks for {artist_name}.")

    def get_top_albums(self, artist_name):
        """
        Get the top albums for a specific artist, including their name, play count,
        and cover art.
        """
        params = {
            'method': 'artist.gettopalbums',
            'artist': artist_name
        }
        try:
            response = self.api.get(params)
            top_albums = response['topalbums']['album']
            return top_albums
        except (KeyError, LastfmError):
            raise LastfmAPIError(f"Failed to get top albums for {artist_name}.")

    def search(self, query):
        """
        Search for artists that match a given query, returning their name, image,
        and Last.fm URL.
        """
        params = {
            'method': 'artist.search',
            'artist': query
        }
        try:
            response = self.api.get(params)
            search_results = response['results']['artistmatches']['artist']
            return search_results
        except (KeyError, LastfmError):
            raise LastfmAPIError(f"No results found for {query}.")

    def get_similar_artists(self, artist_name):
        """
        Get a list of artists that are similar to a specific artist, including their
        name, image, and Last.fm URL.
        """
        params = {
            'method': 'artist.getsimilar',
            'artist': artist_name
        }
        try:
            response = self.api.get(params)
            similar_artists = response['similarartists']['artist']
            return similar_artists
        except (KeyError, LastfmError):
            raise LastfmAPIError(f"Failed to get similar artists for {artist_name}.")
