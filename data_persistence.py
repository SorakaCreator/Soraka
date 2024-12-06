import json
import os
from typing import List, Dict, Any

class DataManager:
    def __init__(self, data_file: str = 'bot_data.json'):
        self.data_file = data_file

    def save_tweets(self, tweets: List[Dict[str, Any]]):
        with open(self.data_file, 'w') as f:
            json.dump(tweets, f)

    def load_tweets(self) -> List[Dict[str, Any]]:
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return []

    def append_tweet(self, tweet: Dict[str, Any]):
        tweets = self.load_tweets()
        tweets.append(tweet)
        self.save_tweets(tweets)

class PerformanceTracker:
    def __init__(self, log_file: str = 'performance_log.txt'):
        self.log_file = log_file

    def log_performance(self, timestamp: float, tweet_count: int, engagement_rate: float):
        with open(self.log_file, 'a') as f:
            f.write(f"{timestamp},{tweet_count},{engagement_rate}\n")

    def get_performance_history(self) -> List[Dict[str, Any]]:
        history = []
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                for line in f:
                    timestamp, tweet_count, engagement_rate = line.strip().split(',')
                    history.append({
                        'timestamp': float(timestamp),
                        'tweet_count': int(tweet_count),
                        'engagement_rate': float(engagement_rate)
                    })
        return history
