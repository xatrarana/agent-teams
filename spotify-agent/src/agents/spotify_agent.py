from google.adk.agents import Agent
from dotenv import load_dotenv
from ..tools.playback_tools import (
    play_music,
    pause_music,
    skip_track,
    previous_track,
    set_volume
)
from ..tools.playlist_tools import (
    get_user_playlists,
    play_playlist,
    search_playlist
)
from ..tools.search_tools import (
    search_track,
    search_artist
)
from ..config.agent_config import AGENT_CONFIG
from ..prompts.instructions import SPOTIFY_AGENT_INSTRUCTIONS


agent_tools = [
    # Playback control
    play_music,
    pause_music,
    skip_track,
    previous_track,
    set_volume,
        
    # Playlist management
    get_user_playlists,
    play_playlist,
    search_playlist,
        
    # Search functionality
    search_track,
    search_artist,
]
    
# Create agent
spotify_agent = Agent(
    model=AGENT_CONFIG['model'],
    name='spotify_agent',
    description='Your personal Spotify DJ and music assistant',
    instruction=SPOTIFY_AGENT_INSTRUCTIONS,
    tools=agent_tools,
    )

root_agent = spotify_agent
    
