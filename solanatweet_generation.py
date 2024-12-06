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
