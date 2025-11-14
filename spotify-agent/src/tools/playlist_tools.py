from ..services.spotify_service import SpotifyService
from ..utils.logger import get_logger

logger = get_logger()
spotify = SpotifyService()


def get_user_playlists() -> dict:
    """
    Get all playlists for the current user
    
    Returns:
        dict: List of user's playlists
    """
    try:
        playlists = spotify.get_playlists()
        logger.info(f"Retrieved {len(playlists)} playlists")
        return {
            "success": True,
            "playlists": playlists,
            "count": len(playlists)
        }
    except Exception as e:
        logger.error(f"Failed to get playlists: {e}")
        return {
            "success": False,
            "error": str(e)
        }


def play_playlist(playlist_name: str) -> dict:
    """
    Play a specific playlist by name
    
    Args:
        playlist_name: Name of the playlist to play
    
    Returns:
        dict: Status of the operation
    """
    try:
        result = spotify.play_playlist_by_name(playlist_name)
        logger.info(f"Playing playlist: {playlist_name}")
        return {
            "success": True,
            "message": f"Now playing: {playlist_name}",
            "data": result
        }
    except Exception as e:
        logger.error(f"Failed to play playlist '{playlist_name}': {e}")
        return {
            "success": False,
            "error": str(e)
        }


def search_playlist(query: str) -> dict:
    """
    Search for playlists by name
    
    Args:
        query: Search query
    
    Returns:
        dict: List of matching playlists
    """
    try:
        results = spotify.search_playlists(query)
        logger.info(f"Found {len(results)} playlists for '{query}'")
        return {
            "success": True,
            "query": query,
            "playlists": results,
            "count": len(results)
        }
    except Exception as e:
        logger.error(f"Failed to search playlists: {e}")
        return {
            "success": False,
            "error": str(e)
        }