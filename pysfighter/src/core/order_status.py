import requests
import json
import StringIO
import pysfighter

def order_status(venue, stock, order):
    response = requests.get("https://api.stockfighter.io/ob/api/venues/"+venue+"/stocks/"+stock+"/orders/"+str(order),
                             headers={"X-Starfighter-Authorization": pysfighter.core.api_key}).text
    response = json.load(StringIO.StringIO(response))
    status = pysfighter.Object()
    
    status.symbol = response["symbol"]
    status.venue = response["venue"]
    status.direction = response["direction"]
    status.originalQty = response["originalQty"]
    status.qty = response["qty"]
    status.price = response["orderType"]
    status.orderType = response["orderType"]
    status.id = response["id"]
    status.account = response["account"]
    status.ts = response["ts"]
    status.totalFilled = response["totalFilled"]
    status.open = response["open"]
    status.fills = []
    status.fills = []
    for f in response["fills"]:
        fill = pysfighter.Object()
        fill.price = f["price"]
        fill.qty = f["qty"]
        fill.ts = f["ts"]
        
    return status