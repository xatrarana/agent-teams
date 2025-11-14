import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ..config.settings import SPOTIFY_CONFIG
from ..utils.logger import get_logger

logger = get_logger()


class SpotifyService:
    """
    Wrapper for Spotify API operations
    """
    
    def __init__(self):
        """Initialize Spotify client with OAuth"""
        self.sp = None
        self._authenticate()
    
    def _authenticate(self):
        """Authenticate with Spotify using OAuth"""
        try:
            scope = "user-read-playback-state,user-modify-playback-state,playlist-read-private,user-library-read"
            
            self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=SPOTIFY_CONFIG['client_id'],
                client_secret=SPOTIFY_CONFIG['client_secret'],
                redirect_uri=SPOTIFY_CONFIG['redirect_uri'],
                scope=scope,
                cache_path=".spotify_cache"
            ))
            
            logger.info("Spotify authentication successful")
        except Exception as e:
            logger.error(f"Spotify authentication failed: {e}")
            raise
    
    # Playback methods
    def resume_playback(self):
        """Resume current playback"""
        return self.sp.start_playback()
    
    def pause_playback(self):
        """Pause current playback"""
        return self.sp.pause_playback()
    
    def next_track(self):
        """Skip to next track"""
        return self.sp.next_track()
    
    def previous_track(self):
        """Go to previous track"""
        return self.sp.previous_track()
    
    def set_volume(self, volume_percent: int):
        """Set playback volume (0-100)"""
        return self.sp.volume(volume_percent)
    
    # Playlist methods
    def get_playlists(self):
        """Get user's playlists"""
        results = self.sp.current_user_playlists()
        playlists = []
        
        for item in results['items']:
            playlists.append({
                'name': item['name'],
                'id': item['id'],
                'tracks': item['tracks']['total']
            })
        
        return playlists
    
    def play_playlist_by_name(self, playlist_name: str):
        """Play a playlist by name"""
        playlists = self.get_playlists()
        
        for playlist in playlists:
            if playlist_name.lower() in playlist['name'].lower():
                return self.sp.start_playback(context_uri=f"spotify:playlist:{playlist['id']}")
        
        raise ValueError(f"Playlist '{playlist_name}' not found")
    
    def search_playlists(self, query: str):
        """Search for playlists"""
        results = self.sp.search(q=query, type='playlist', limit=10)
        playlists = []
        
        for item in results['playlists']['items']:
            playlists.append({
                'name': item['name'],
                'id': item['id'],
                'owner': item['owner']['display_name']
            })
        
        return playlists
    
    # Search methods
    def search_tracks(self, query: str):
        """Search for tracks"""
        results = self.sp.search(q=query, type='track', limit=10)
        tracks = []
        
        for item in results['tracks']['items']:
            tracks.append({
                'name': item['name'],
                'artist': item['artists'][0]['name'],
                'album': item['album']['name'],
                'id': item['id']
            })
        
        return tracks
    
    def search_artists(self, query: str):
        """Search for artists"""
        results = self.sp.search(q=query, type='artist', limit=10)
        artists = []
        
        for item in results['artists']['items']:
            artists.append({
                'name': item['name'],
                'id': item['id'],
                'followers': item['followers']['total']
            })
        
        return artists