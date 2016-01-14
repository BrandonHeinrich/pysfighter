import requests
import json
import StringIO

def venue_heartbeat(venue):
    response = requests.get("https://api.stockfighter.io/ob/api/venues/"+venue+"/heartbeat").text
    hb = json.load(StringIO.StringIO(response))
    return hb