import logging
import os
from ..config.settings import LOGGING_CONFIG


def setup_logger():
    """Setup application logger"""
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, LOGGING_CONFIG['level']),
        format=LOGGING_CONFIG['format'],
        handlers=[
            logging.FileHandler(LOGGING_CONFIG['file']),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger('spotify_agent')


def get_logger():
    """Get the application logger"""
    return logging.getLogger('spotify_agent')