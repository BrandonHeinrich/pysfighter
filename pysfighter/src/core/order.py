import requests
import json
import StringIO
import pysfighter

def order(account, venue, symbol, price, qty, direction, orderType):
    order = {
          "account":    account,
          "venue":      venue,
          "symbol":     symbol,
          "price":      price,
          "qty":        qty,
          "direction":  direction,
          "orderType":  orderType
        }
    response = requests.post("https://api.stockfighter.io/ob/api/venues/"+venue+"/stocks/"+symbol+"/orders",
                             data=json.dumps(order),
                             headers={"X-Starfighter-Authorization": pysfighter.core.api_key}).text
    response = json.load(StringIO.StringIO(response))
    
    order = pysfighter.Object()
    
    order.symbol = response["symbol"]
    order.venue = response["venue"]
    order.direction = response["direction"]
    order.originalQty = response["originalQty"]
    order.qty = response["qty"]
    order.orderType = response["orderType"]
    order.id = response["id"]
    order.account = response["account"]
    order.ts = response["ts"]
    order.totalFilled = response["totalFilled"]
    order.open = response["open"]
    order.fills = []
    for f in response["fills"]:
        fill = pysfighter.Object()
        fill.price = f["price"]
        fill.qty = f["qty"]
        fill.ts = f["ts"]
        order.fills.append(fill)
        
    return order