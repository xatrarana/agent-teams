
from .agents.spotify_agent import root_agent

__all__ = ["root_agent"]

# Load environment variables
# load_dotenv()

# create_spotify_agent();

# # def main():
#     """Main entry point for the Spotify Agent application"""
#     logger.info("Starting Spotify Agent...")
    
#     # Create the agent
#     agent = create_spotify_agent()
    
#     # Interactive loop
#     print("🎵 Spotify Agent Ready! Type 'quit' to exit.\n")
    
#     while True:
#         try:
#             user_input = input("You: ").strip()
            
#             if user_input.lower() in ['quit', 'exit', 'bye']:
#                 print("👋 Goodbye!")
#                 break
            
#             if not user_input:
#                 continue
            
#             # Send to agent
#             response = agent.send_message(user_input)
#             print(f"\n🤖 Agent: {response}\n")
            
#         except KeyboardInterrupt:
#             print("\n👋 Goodbye!")
#             break
#         except Exception as e:
#             logger.error(f"Error: {e}")
#             print(f"❌ Error: {e}\n")

# if __name__ == "__main__":
#     main()