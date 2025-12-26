#!/usr/bin/env python3

"""
Demonstrate basic HTTP requests in Python using the requests' library.

This module serves as the entry point for the codebase and provides
a simple example of fetching JSON data from a REST API.
"""
from src import basic_request, kraken_request, llm_client


def main():
    post = basic_request.fetch_post()
    print(f"Post: {post}")
    btc_price = kraken_request.get_btc_price()
    print(f"BTC Price: {btc_price}")
    # call functions from llm_client.py
    grok_result = llm_client.analyze_with_grok("What is the current date and time in New York City?")
    print(f"Grok Result: {grok_result}")


if __name__ == "__main__":
    main()
