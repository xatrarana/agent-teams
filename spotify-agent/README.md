# 🎵 Spotify Agent with Google ADK

AI-powered Spotify controller using Google's Agent Development Kit.

## Features
- 🎮 Playback control (play, pause, skip, volume)
- 📝 Playlist management
- 🔍 Music search
- 🤖 Natural language interface

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get Spotify Credentials
1. Go to https://developer.spotify.com/dashboard
2. Create a new app
3. Copy Client ID and Client Secret
4. Add redirect URI: `http://localhost:8888/callback`

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env with your credentials
```

### 4. Run the Agent
```bash
python src/main.py
```

## Project Structure
```
spotify-agent/
├── src/
│   ├── main.py              # Entry point
│   ├── agents/              # Agent definitions
│   ├── tools/               # Agent tools
│   ├── services/            # Spotify API wrapper
│   ├── config/              # Configuration
│   ├── prompts/             # Agent instructions
│   └── utils/               # Utilities
├── logs/                    # Log files
├── requirements.txt
├── .env.example
└── README.md
```

## Usage Examples

```
You: Play my workout playlist
Agent: Playing your 'Beast Mode' playlist! 🎵

You: Skip this song
Agent: Skipped! ⏭️ Next track coming up.

You: Set volume to 50
Agent: Volume set to 50% 🔊

You: Search for jazz music
Agent: Found these jazz tracks: [list of tracks]
```

## Troubleshooting

**Authentication Error:**
- Make sure your Spotify credentials are correct in `.env`
- Check that redirect URI matches in Spotify Dashboard

**No Active Device:**
- Open Spotify app on your device
- Start playing something first

## License
MIT