import os
from dotenv import load_dotenv

load_dotenv()

# Spotify Configuration
SPOTIFY_CONFIG = {
    'client_id': os.getenv('SPOTIFY_CLIENT_ID', ''),
    'client_secret': os.getenv('SPOTIFY_CLIENT_SECRET', ''),
    'redirect_uri': os.getenv('SPOTIFY_REDIRECT_URI', 'http://localhost:8888/callback'),
}

# Logging Configuration
LOGGING_CONFIG = {
    'level': os.getenv('LOG_LEVEL', 'INFO'),
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'logs/spotify_agent.log'
}