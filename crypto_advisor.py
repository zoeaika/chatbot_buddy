# crypto_advisor.py
# Main chatbot logic

from crypto_data import crypto_db

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.greeting = "🚀 Hey there! I'm CryptoBuddy, your crypto investment sidekick! Let's find you some great coins! 💰"
    
    def greet(self):
        print(self.greeting)
        print("\nI can help you with:")
        print("- Finding trending cryptocurrencies")
        print("- Sustainable and eco-friendly coins")
        print("- Profitable investment opportunities")
        print("- General crypto advice")
        print("\nType 'quit' or 'exit' to end our chat!\n")
    
    def analyze_query(self, user_input):
        """Analyze user input and provide appropriate response"""
        query = user_input.lower()
        
        # Sustainability queries
        if any(word in query for word in ["sustainable", "eco", "green", "environment", "energy"]):
            return self.get_sustainable_recommendation()
        
        # Profitability queries
        elif any(word in query for word in ["profit", "rising", "trending", "growth", "buy", "invest"]):
            return self.get_profitable_recommendation()
        
        # High market cap queries
        elif any(word in query for word in ["safe", "stable", "secure", "reliable"]):
            return self.get_safe_recommendation()
        
        # Specific coin queries
        elif any(coin.lower() in query for coin in crypto_db.keys()):
            return self.get_specific_coin_info(query)
        
        # Price queries
        elif "price" in query:
            return self.get_price_info()
        
        # Default response
        else:
            return self.get_general_advice()
    
    def get_sustainable_recommendation(self):
        """Find most sustainable cryptocurrency"""
        sustainable_coins = {coin: data for coin, data in crypto_db.items() 
                           if data["sustainability_score"] >= 7}
        
        if sustainable_coins:
            best_coin = max(sustainable_coins, key=lambda x: sustainable_coins[x]["sustainability_score"])
            score = crypto_db[best_coin]["sustainability_score"]
            return f"🌱 {best_coin} ({crypto_db[best_coin]['symbol']}) is your best eco-friendly choice! It has a sustainability score of {score}/10 and uses {crypto_db[best_coin]['energy_use']} energy. Great for long-term green investing! 🌿"
        else:
            return "🌱 For sustainability, I'd recommend Cardano (ADA) or Solana (SOL) - both are eco-friendly options!"
    
    def get_profitable_recommendation(self):
        """Find most profitable cryptocurrency"""
        rising_coins = {coin: data for coin, data in crypto_db.items() 
                       if data["price_trend"] == "rising"}
        
        if rising_coins:
            # Prioritize high market cap among rising coins
            best_coin = max(rising_coins, key=lambda x: 
                          (rising_coins[x]["market_cap"] == "high", rising_coins[x]["sustainability_score"]))
            
            return f"📈 {best_coin} ({crypto_db[best_coin]['symbol']}) is trending up! Current price: ${crypto_db[best_coin]['current_price']:,}. It has {crypto_db[best_coin]['market_cap']} market cap and {crypto_db[best_coin]['project_viability']} project viability. 🚀"
        else:
            return "📈 Right now, Bitcoin and Ethereum are showing strong upward trends!"
    
    def get_safe_recommendation(self):
        """Find safest cryptocurrency investment"""
        safe_coins = {coin: data for coin, data in crypto_db.items() 
                     if data["market_cap"] == "high" and data["project_viability"] == "excellent"}
        
        if safe_coins:
            coin_list = ", ".join([f"{coin} ({data['symbol']})" for coin, data in safe_coins.items()])
            return f"🛡️ For safe investments, consider: {coin_list}. These have high market caps and excellent project viability!"
        else:
            return "🛡️ Bitcoin and Ethereum are generally considered the safest crypto investments due to their established market presence!"
    
    def get_specific_coin_info(self, query):
        """Get information about a specific cryptocurrency"""
        for coin, data in crypto_db.items():
            if coin.lower() in query:
                trend_emoji = "📈" if data["price_trend"] == "rising" else "📉" if data["price_trend"] == "falling" else "➡️"
                return f"{trend_emoji} {coin} ({data['symbol']}) Info:\n💰 Price: ${data['current_price']:,}\n📊 Trend: {data['price_trend']}\n🌍 Sustainability: {data['sustainability_score']}/10\n⚡ Energy Use: {data['energy_use']}\n🏗️ Project Viability: {data['project_viability']}"
        
        return "🤔 I don't have information about that specific coin. Try asking about Bitcoin, Ethereum, Cardano, Solana, Dogecoin, or Polygon!"
    
    def get_price_info(self):
        """Show current prices of all cryptocurrencies"""
        price_info = "💰 Current Crypto Prices:\n"
        for coin, data in crypto_db.items():
            trend_emoji = "📈" if data["price_trend"] == "rising" else "📉" if data["price_trend"] == "falling" else "➡️"
            price_info += f"{trend_emoji} {coin} ({data['symbol']}): ${data['current_price']:,}\n"
        return price_info
    
    def get_general_advice(self):
        """Provide general cryptocurrency advice"""
        advice_list = [
            "💡 Always do your own research before investing!",
            "🌱 Consider the environmental impact - choose sustainable coins!",
            "📊 Look for coins with strong project fundamentals and good viability!",
            "💰 Diversify your portfolio - don't put all eggs in one basket!",
            "📈 Check the price trends and market cap before investing!"
        ]
        
        import random
        return f"Here's some crypto wisdom: {random.choice(advice_list)}\n\n🤖 Ask me about specific coins, sustainability, or profitability for more targeted advice!"
    
    def chat(self):
        """Main chat loop"""
        self.greet()
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("CryptoBuddy: Thanks for chatting! Happy investing! 🚀💰")
                break
            
            if not user_input:
                print("CryptoBuddy: I'm here to help! Ask me anything about crypto! 😊")
                continue
            
            response = self.analyze_query(user_input)
            print(f"CryptoBuddy: {response}\n")

# Run the chatbot
if __name__ == "__main__":
    bot = CryptoBuddy()
    bot.chat()