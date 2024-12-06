import time
import threading
import logging
from twitter_api import TwitterAPI, RateLimiter
from tweet_generation import SorakaTweetGenerator, TweetQueue

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TwitterBot:
    def __init__(self, api: TwitterAPI, tweet_generator: SorakaTweetGenerator, post_interval: float):
        self.api = api
        self.tweet_generator = tweet_generator
        self.post_interval = post_interval
        self.tweet_queue = TweetQueue()
        self.rate_limiter = RateLimiter(max_requests=300, time_window=900)  # 300 requests per 15 minutes
        self.running = False

    def start(self):
        self.running = True
        threading.Thread(target=self._tweet_worker, daemon=True).start()
        threading.Thread(target=self._queue_filler, daemon=True).start()

    def stop(self):
        self.running = False

    def _tweet_worker(self):
        while self.running:
            if not self.tweet_queue.is_empty() and self.rate_limiter.can_make_request():
                tweet = self.tweet_queue.get_tweet()
                self.api.post_tweet(tweet)
                self.rate_limiter.add_request()
            time.sleep(self.post_interval)

    def _queue_filler(self):
        while self.running:
            if self.tweet_queue.queue.qsize() < 50:
                tweet = self.tweet_generator.generate_tweet()
                self.tweet_queue.add_tweet(tweet)
            time.sleep(1)

def main():
    # Initialize TwitterAPI (with dummy credentials)
    api = TwitterAPI("api_key", "api_secret", "access_token", "access_token_secret")
    
    # Initialize SorakaTweetGenerator
    tweet_generator = SorakaTweetGenerator()
    
    # Initialize and start the TwitterBot
    bot = TwitterBot(api, tweet_generator, post_interval=2.0)
    bot.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Received interrupt. Stopping the bot...")
        bot.stop()

if __name__ == "__main__":
    main()
