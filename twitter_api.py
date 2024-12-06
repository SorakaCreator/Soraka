import time
import hashlib
import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TwitterAPI:
    def __init__(self, api_key: str, api_secret: str, access_token: str, access_token_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        logger.info("TwitterAPI initialized with provided credentials")

    def authenticate(self) -> bool:
        time.sleep(0.5)
        logger.info("Authentication successful")
        return True

    def post_tweet(self, content: str) -> Dict[str, Any]:
        tweet_id = hashlib.md5(content.encode()).hexdigest()
        logger.info(f"Tweet posted successfully. Tweet ID: {tweet_id}")
        return {"id": tweet_id, "text": content, "created_at": time.time()}

    def get_user_timeline(self, user_id: str, count: int = 20) -> List[Dict[str, Any]]:
        return [{"id": f"tweet_{i}", "text": f"Sample tweet {i}", "created_at": time.time()} for i in range(count)]

class RateLimiter:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.request_times = []

    def add_request(self):
        current_time = time.time()
        self.request_times.append(current_time)
        self.request_times = [t for t in self.request_times if current_time - t <= self.time_window]

    def can_make_request(self) -> bool:
        return len(self.request_times) < self.max_requests

class TwitterAnalytics:
    @staticmethod
    def calculate_engagement_rate(impressions: int, interactions: int) -> float:
        return (interactions / impressions) * 100 if impressions > 0 else 0

    @staticmethod
    def analyze_hashtags(tweets: List[Dict[str, Any]]) -> Dict[str, int]:
        hashtag_counts = {}
        for tweet in tweets:
            hashtags = [word for word in tweet['text'].split() if word.startswith('#')]
            for hashtag in hashtags:
                hashtag_counts[hashtag] = hashtag_counts.get(hashtag, 0) + 1
        return hashtag_counts
