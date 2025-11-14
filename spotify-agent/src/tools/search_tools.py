from ..services.spotify_service import SpotifyService
from ..utils.logger import get_logger

logger = get_logger()
spotify = SpotifyService()


def search_track(query: str) -> dict:
    """
    Search for tracks by name
    
    Args:
        query: Search query
    
    Returns:
        dict: List of matching tracks
    """
    try:
        results = spotify.search_tracks(query)
        logger.info(f"Found {len(results)} tracks for '{query}'")
        return {
            "success": True,
            "query": query,
            "tracks": results,
            "count": len(results)
        }
    except Exception as e:
        logger.error(f"Failed to search tracks: {e}")
        return {
            "success": False,
            "error": str(e)
        }


def search_artist(query: str) -> dict:
    """
    Search for artists by name
    
    Args:
        query: Artist name to search
    
    Returns:
        dict: List of matching artists
    """
    try:
        results = spotify.search_artists(query)
        logger.info(f"Found {len(results)} artists for '{query}'")
        return {
            "success": True,
            "query": query,
            "artists": results,
            "count": len(results)
        }
    except Exception as e:
        logger.error(f"Failed to search artists: {e}")
        return {
            "success": False,
            "error": str(e)
        }