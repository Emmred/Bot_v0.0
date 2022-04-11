from flask import Flask, request, abort
########################################
import json
import requests
########################################
webhook_url = 'https://webhook.site/3ce008d7-5362-400d-ac7d-575fa8fd582f' #"http://127.0.0.1:5000/webhook"
data = {'':''}
name = ''
secret = ''
symbol = {'':''}
########################################
app= Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)

        data={
        "name": name,
        "secret": secret,
        "side": "buy",
        "symbol": request.json['symbol']
        }
        r = requests.post(webhook_url,data=json.dumps(data),headers={'content-type':'application/json'})
        return 'succes',200
    else:
        abort(400)

@app.route('/')
def test():
    return 'hola mundo'

if __name__ == '__main__':
    app.run(debug=True)

########################################