# Soraka $SOL Twitter Bot

## [Visit Twitter Page](https://x.com/SolMaxiAI)

## Overview

Soraka is an AI Solana Maxi sophisticated Python-based application that simulates an automated Twitter bot designed to generate and spread facts and disadvantages. This project demonstrates advanced programming concepts such as multi-threading, queue management, rate limiting, and API integration.

**Note**: This bot does not actually post to Twitter. It's a simulation for educational and entertainment purposes only.

## Project Structure

The project is organized into several Python modules, each responsible for specific functionalities:

1. `soraka_ai.py`: Contains the core Soraka class for generating facts related to Solana.
2. `twitter_api.py`: Simulates interaction with the Twitter API, including posting tweets and rate limiting.
3. `tweet_generation.py`: Manages tweet generation and queue management.
4. `Soraka_bot_runner.py`: The main script that ties everything together and runs the bot.
5. `config.py`: Centralizes configuration settings for easy management.
6. `logger.py`: Sets up a custom logging system for consistent logging across all modules.

## Key Features

- **Solana Maxi Generation**: Utilizes a active list of facts and disadvatages of Solana to simulate the generation of "Solana" tweets.
- **Tweet Queue Management**: Implements a thread-safe queue to manage generated tweets before posting.
- **Rate Limiting**: Simulates Twitter's rate limiting to demonstrate responsible API usage.
- **Multi-threading**: Uses separate threads for tweet generation and posting to improve efficiency.
- **Configurable Settings**: Allows easy customization of bot behavior through a central configuration file.
- **Comprehensive Logging**: Provides detailed logs of bot activities for monitoring and debugging.

## How It Works

1. The bot initializes by setting up the Twitter API simulation and the Soraka tweet generator.
2. Two main threads are started:
   - A queue filler thread that continuously generates new Soraka tweets.
   - A worker thread that posts tweets from the queue at regular intervals.
3. The bot simulates posting tweets, respecting a configured rate limit.
4. Detailed logs are generated to track the bot's activities.
5. The bot can be gracefully shut down using a keyboard interrupt (Ctrl+C).

## Setup and Running

1. Ensure you have Python 3.7+ installed on your system.
2. Clone this repository:
