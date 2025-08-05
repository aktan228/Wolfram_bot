import os
import requests


def query_wolfram(query: str) -> str:
    app_id = os.getenv("WOLFRAM_APP_ID")
    url = "http://api.wolframalpha.com/v2/query"

    params = {
        "input": query,
        "format": "plaintext,latex",
        "output": "JSON",
        "appid": app_id,
    }
    res = requests.get(url, params=params).json()

    try:
        pods = res["queryresult"]["pods"]
        for pod in pods:
            subpod = pod["subpods"][0]
            if "latex" in subpod and subpod["latex"].strip():
                return {"latex": subpod["latex"]}
            elif "plaintext" in subpod and["latex"].strip():
                return {"plaintex": subpod["plaintext"]}
        return {"error":"No results found"}
    except Exception:
        return {"error":"Error processing in query"}

# {
#   "queryresult": {
#     "pods": [
#       {
#         "title": "Result",
#         "subpods": [
#           {
#             "plaintext": "x^2 + y^2",
#             "latex": "x^{2}+y^{2}"
#           }
#         ]
#       }
#     ]
#   }
# }
