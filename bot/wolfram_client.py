import os
import requests


def query_wolfram(query: str) -> str:
    app_id = os.getenv("WOLFRAM_APP_ID")
    url = "http://api.wolframalpha.com/v2/query"

    params = {
        "input":query,
        "format":"plaintext,latex",
        "output":"JSON",
        "appid":app_id
    }
    res = requests.get(url,params=params).json()
    
    try:
        pods = res["queryresult"]["pods"]
        for pod in pods:
            if "plaintext" in pod["subpods"][0]:
                return pod["subpods"][0]["plaintext"]
        return "No results found"
    except Exception:
        return "Error processing in query"
    
    
    
    
    # params = {
    #     "input": query,
    #     "format": "plaintext",
    #     "output": "JSON",
    #     "appid": app_id
    # }

    # res = requests.get(url, params=params).json()

    # try:
    #     pods = res["queryresult"]["pods"]
    #     for pod in pods:
    #         if "plaintext" in pod["subpods"][0]:
    #             return pod["subpods"][0]["plaintext"]
    #     return "No result found."
    # except Exception:
    #     return "Error processing the query."