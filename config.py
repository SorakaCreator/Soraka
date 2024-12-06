# config.py

# Twitter API Configuration (dummy values)
TWITTER_API_KEY = "your_api_key"
TWITTER_API_SECRET = "your_api_secret"
TWITTER_ACCESS_TOKEN = "your_access_token"
TWITTER_ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Bot Configuration
POST_INTERVAL = 2.0  # Time between posts in seconds
MAX_QUEUE_SIZE = 100  # Maximum number of tweets to keep in the queue
RATE_LIMIT_MAX_REQUESTS = 300  # Maximum number of requests allowed
RATE_LIMIT_WINDOW = 900  # Time window for rate limiting in seconds (15 minutes)

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "Soraka_bot.log"
