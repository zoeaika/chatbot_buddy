# main.py
# Simple entry point to run the chatbot

from crypto_advisor import CryptoBuddy

def main():
    """Main function to start the CryptoBuddy chatbot"""
    print("=" * 50)
    print("  Welcome to CryptoBuddy - Your Crypto Advisor!")
    print("=" * 50)
    
    # Create and start the chatbot
    buddy = CryptoBuddy()
    buddy.chat()

if __name__ == "__main__":
    main()