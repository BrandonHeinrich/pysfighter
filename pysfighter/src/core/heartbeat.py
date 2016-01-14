import requests
import json
import StringIO

def heartbeat():
    response = requests.get("https://api.stockfighter.io/ob/api/heartbeat").text
    hb = json.load(StringIO.StringIO(response))
    hb["error"] = str(hb["error"])
    return hb