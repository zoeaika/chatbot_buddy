class CryptoAdvisor:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.greeting = "🌟 Hey there, crypto explorer! I'm your AI-powered financial sidekick. Let's find you some green and growing digital assets! 🌱"
        self.farewell = "🚀 Happy investing! Remember to DYOR (Do Your Own Research) and never invest more than you can afford to lose!"
        
        # Crypto database with price trends, sustainability, and other metrics
        self.crypto_db = {  
            "Bitcoin": {  
                "price_trend": "rising",  
                "market_cap": "high",  
                "energy_use": "high",  
                "sustainability_score": 3/10,
                "volatility": "high"
            },  
            "Ethereum": {  
                "price_trend": "stable",  
                "market_cap": "high",  
                "energy_use": "medium",  
                "sustainability_score": 6/10,
                "volatility": "medium"
            },  
            "Cardano": {  
                "price_trend": "rising",  
                "market_cap": "medium",  
                "energy_use": "low",  
                "sustainability_score": 8/10,
                "volatility": "medium"
            },
            "Solana": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7/10,
                "volatility": "high"
            },
            "Algorand": {
                "price_trend": "stable",
                "market_cap": "low",
                "energy_use": "low",
                "sustainability_score": 9/10,
                "volatility": "low"
            }
        }
        
        # Common user queries and keywords
        self.keywords = {
            "sustainability": ["sustainable", "green", "eco", "environment", "energy"],
            "profitability": ["profit", "grow", "trend", "rising", "perform", "return"],
            "stable": ["stable", "safe", "low risk", "secure"],
            "volatile": ["volatile", "high risk", "speculative"],
            "popular": ["popular", "well-known", "established", "big"]
        }
    
    def start_chat(self):
        print(f"\n{self.greeting}\n")
        print("I can help you with:\n- Trending cryptocurrencies\n- Sustainable/eco-friendly coins\n- Stable vs high-growth options\n- General crypto advice\n")
        
        while True:
            user_input = input("\nWhat would you like to know? (or type 'quit' to exit): ").lower()
            
            if user_input == 'quit':
                print(f"\n{self.farewell}\n")
                break
                
            self.analyze_query(user_input)
    
    def analyze_query(self, query):
        # Check for sustainability-related queries
        if any(word in query for word in self.keywords["sustainability"]):
            self.recommend_sustainable()
        
        # Check for profitability-related queries
        elif any(word in query for word in self.keywords["profitability"]):
            self.recommend_profitable()
        
        # Check for stable/low-risk queries
        elif any(word in query for word in self.keywords["stable"]):
            self.recommend_stable()
        
        # Check for volatile/high-risk queries
        elif any(word in query for word in self.keywords["volatile"]):
            self.recommend_volatile()
        
        # Check for popular/established queries
        elif any(word in query for word in self.keywords["popular"]):
            self.recommend_popular:()
        
        # Default response for unrecognized queries
        else:
            print("🤔 I'm not sure I understand. Try asking about sustainable cryptos, trending coins, or stable investments!")
    
    def recommend_sustainable(self):
        recommend = max(self.crypto_db, key=lambda x: self.crypto_db[x]["sustainability_score"])
        score = self.crypto_db[recommend]["sustainability_score"]
        print(f"🌱 Based on sustainability, I recommend {recommend} with a score of {score*10}/10!")
        print(f"💡 Details: Energy use is {self.crypto_db[recommend]['energy_use']} and price trend is {self.crypto_db[recommend]['price_trend']}.")
    
    def recommend_profitable(self):
        # Filter coins with rising trends and high market cap
        profitable_coins = [
            (name, data) for name, data in self.crypto_db.items() 
            if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]
        ]
        
        if profitable_coins:
            print("📈 Currently trending up with good market cap:")
            for coin, data in profitable_coins:
                print(f"- {coin}: Market cap is {data['market_cap']}, sustainability score {data['sustainability_score']*10}/10")
        else:
            print("⚠️ No strongly trending coins found in our database currently.")
    
    def recommend_stable(self):
        stable_coins = [
            (name, data) for name, data in self.crypto_db.items()
            if data["volatility"] == "low" and data["price_trend"] == "stable"
        ]
        
        if stable_coins:
            print("🛡️ Lower-risk, more stable options:")
            for coin, data in stable_coins:
                print(f"- {coin}: Volatility is {data['volatility']}, price trend is {data['price_trend']}")
        else:
            print("ℹ️ All cryptocurrencies carry some risk. For the most stable options, consider established coins like Bitcoin or Ethereum.")
    
    def recommend_volatile(self):
        volatile_coins = [
            (name, data) for name, data in self.crypto_db.items()
            if data["volatility"] == "high" and data["price_trend"] == "rising"
        ]
        
        if volatile_coins:
            print("🎢 Higher-risk, potentially higher-reward options:")
            for coin, data in volatile_coins:
                print(f"- {coin}: Very volatile but currently trending up")
            print("⚠️ Warning: These are speculative investments with higher risk!")
        else:
            print("ℹ️ Currently no extremely volatile coins in our database are showing strong upward trends.")
    
    def recommend_popular(self):
        popular_coins = [
            (name, data) for name, data in self.crypto_db.items()
            if data["market_cap"] == "high"
        ]
        
        if popular_coins:
            print("🏆 Most established cryptocurrencies:")
            for coin, data in popular_coins:
                print(f"- {coin}: Market cap is {data['market_cap']}, {data['sustainability_score']*10}/10 sustainability")
        else:
            print("ℹ️ Check the top 10 on CoinMarketCap for the most popular cryptos!")

# Start the chatbot
if __name__ == "__main__":
    advisor = CryptoAdvisor()
    advisor.start_chat()