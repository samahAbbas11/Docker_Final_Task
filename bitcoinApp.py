from flask import Flask, render_template, request
import datetime
import requests

app = Flask(__name__)


now = datetime.datetime.now()

#  get current date in this format dd/mm/YY
curr_date = now.strftime("%d/%m/%Y %H:%M:%S")



# this function gets the current price of BITCOIN
def get_current_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = (requests.get(url))
    data = response.json()
    price = data['bpi']["USD"]['rate']

    return ""+str(curr_date)+" --> "+str(price)+"$"

# this function calculates the average prices of BITCOIN for the last 10 minutes
def get_10mins_avrg():
    url = "https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10"
    response = (requests.get(url))
    data = response.json()
    prices =[] #prices list for the last 10 minutes
    # i = [0,1,....,9]
    for i in range(10):
        price = data['Data']["Data"][i]['close']
        prices.append(price)

    average = sum(prices) / len(prices) #the average of the prices 
    return "Average "+" --> "+str(average)+"$"


@app.route('/')
def index_route():
    return render_template('index.html',message1=get_current_price(),message2=get_10mins_avrg())



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)