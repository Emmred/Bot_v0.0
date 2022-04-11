import json
import requests

webhook_url = 'https://parseapi.back4app.com/webhook' #'https://hook.finandy.com/5j4cCbAJqJhI6dNoq1UK' #"http://127.0.0.1:5000/webhook"
data={
  "name": "ETF maestro",
  "secret": "whym82qagv",
  "side": "sell",
  "symbol": "BNBUSDT",
  "open": {
    "amountType": "amount",
    "amount": "0.033"
  }
}


r = requests.post(webhook_url,data=json.dumps(data),headers={'content-type':'application/json'})