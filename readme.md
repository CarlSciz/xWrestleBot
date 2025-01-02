<div align="center">
  <img src="media/xwrestlebot.jpeg" alt="xWrestleBot Logo" width="300">
  <h1>xWrestleBot</h1>
  <p>A bot that promotes this date in history main event wrestling facts, straight from the squared circle!</p>
</div>

---

## ⚡️ Quick Start

1. **Clone the repository:**
   ```bash
   git clone git@github.com:CarlSciz/xwrestlebot.git
   cd 
   
2. **Set up virtual environment:**
   ```bash
    python -m venv venv
    source venv/bin/activate    # On macOS/Linux
    .\venv\Scripts\activate     # On Windows

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Create a .env file:**
   ```bash
   API_KEY=your_api_key
   API_SECRET_KEY=your_api_secret_key
   ACCESS_TOKEN=your_access_token
   ACCESS_TOKEN_SECRET=your_access_token_secret
   BEARER_TOKEN=your_bearer_token

5. **Run the bot:**
   ```bash
   python post_wrestling_facts.py 

## ⚙️ Features 

- 📅 Retrieves historical wrestling match card event data from [ProFightDB](http://www.profightdb.com/this-day-in-history.html) based on the current date.

- 🎲 Randomly selects a match card that is at least 10 years or older.
- 🐦 Posts main event details from the selected match card on Twitter/X leveraging the API via Tweepy.
- 🌐 Uses BeautifulSoup for web scraping to parse and extract data for custom logic.

## ✨ Requirements

- Python 3.7+
- Tweepy
- BeautifulSoup
- dotenv

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for more details.