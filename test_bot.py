# test_bot.py
# Test the chatbot functionality

from crypto_advisor import CryptoBuddy

def test_chatbot():
    """Test different chatbot responses"""
    bot = CryptoBuddy()
    
    print("🧪 Testing CryptoBuddy Responses:")
    print("=" * 40)
    
    # Test cases
    test_queries = [
        "Which crypto is most sustainable?",
        "What's trending up right now?",
        "Tell me about Bitcoin",
        "Show me current prices",
        "What's a safe investment?",
        "Which coin should I buy for profit?"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{i}. Test Query: '{query}'")
        print("-" * 30)
        response = bot.analyze_query(query)
        print(f"CryptoBuddy: {response}")
    
    print("\n" + "=" * 40)
    print("✅ All tests completed!")

if __name__ == "__main__":
    test_chatbot()