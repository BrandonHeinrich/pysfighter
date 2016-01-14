import requests
import json
import StringIO

def stocks_on_venue(venue):
    response = requests.get("https://api.stockfighter.io/ob/api/venues/"+venue+"/stocks").text
    response = json.load(StringIO.StringIO(response))
    
    stocks = response["symbols"]
    stocks = map(lambda x: str(x["symbol"]), stocks)
    
    return stocks