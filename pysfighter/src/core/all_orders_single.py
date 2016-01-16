import requests
import json
import StringIO
import pysfighter

def all_orders_single(venue, account, stock):
    
    response = requests.get("https://api.stockfighter.io/ob/api/venues/"+venue+"/accounts/"+account+"/stocks/"+stock+"/orders",
                             headers={"X-Starfighter-Authorization": pysfighter.core.api_key}).text
    response = json.load(StringIO.StringIO(response))
    
    orders = pysfighter.Object()
    orders.venue = response["venue"]
    orders.orders = []
    for data in response["orders"]:
        order = pysfighter.Object()
        
        order.symbol = data["symbol"]
        order.venue = data["venue"]
        order.direction = data["direction"]
        order.originalQty = data["originalQty"]
        order.qty = data["qty"]
        order.orderType = data["orderType"]
        order.id = data["id"]
        order.account = data["account"]
        order.ts = data["ts"]
        order.totalFilled = data["totalFilled"]
        order.open = data["open"]
        order.fills = []
        for f in data["fills"]:
            fill = pysfighter.Object()
            fill.price = f["price"]
            fill.qty = f["qty"]
            fill.ts = f["ts"]
            order.fills.append(fill)
            
        orders.orders.append(order)
    return orders