from ..services.spotify_service import SpotifyService
from ..utils.logger import get_logger

logger = get_logger()
spotify = SpotifyService()


def play_music() -> dict:
    """
    Resume playback of the current track
    
    Returns:
        dict: Status of the playback operation
    """
    try:
        result = spotify.resume_playback()
        logger.info("Playback resumed")
        return {
            "success": True,
            "message": "Music resumed",
            "data": result
        }
    except Exception as e:
        logger.error(f"Failed to play music: {e}")
        return {
            "success": False,
            "error": str(e)
        }


def pause_music() -> dict:
    """
    Pause the current playback
    
    Returns:
        dict: Status of the pause operation
    """
    try:
        result = spotify.pause_playback()
        logger.info("Playback paused")
        return {
            "success": True,
            "message": "Music paused",
            "data": result
        }
    except Exception as e:
        logger.error(f"Failed to pause music: {e}")
        return {
            "success": False,
            "error": str(e)
        }


def skip_track() -> dict:
    """
    Skip to the next track
    
    Returns:
        dict: Status of the skip operation
    """
    try:
        result = spotify.next_track()
        logger.info("Skipped to next track")
        return {
            "success": True,
            "message": "Skipped to next track",
            "data": result
        }
    except Exception as e:
        logger.error(f"Failed to skip track: {e}")
        return {
            "success": False,
            "error": str(e)
        }


def previous_track() -> dict:
    """
    Go back to the previous track
    
    Returns:
        dict: Status of the operation
    """
    try:
        result = spotify.previous_track()
        logger.info("Went back to previous track")
        return {
            "success": True,
            "message": "Playing previous track",
            "data": result
        }
    except Exception as e:
        logger.error(f"Failed to go to previous track: {e}")
        return {
            "success": False,
            "error": str(e)
        }


def set_volume(level: int) -> dict:
    """
    Set the playback volume
    
    Args:
        level: Volume level (0-100)
    
    Returns:
        dict: Status of the volume change
    """
    try:
        if not 0 <= level <= 100:
            return {
                "success": False,
                "error": "Volume must be between 0 and 100"
            }
        
        result = spotify.set_volume(level)
        logger.info(f"Volume set to {level}")
        return {
            "success": True,
            "message": f"Volume set to {level}%",
            "data": result
        }
    except Exception as e:
        logger.error(f"Failed to set volume: {e}")
        return {
            "success": False,
            "error": str(e)
        }