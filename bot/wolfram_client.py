import os
import requests


def query_wolfram(query: str) -> str:
    app_id = os.getenv("WOLFRAM_APP_ID")
    url = "http://api.wolframalpha.com/v2/query"

    