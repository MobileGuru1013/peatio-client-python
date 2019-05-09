import time
from lib.client import Client, get_api_path
import numpy as np
import time

client1 = Client(access_key='XcFvxAdM1iupNh3Q0glbzicvm3ASMEEhzmQjQ7MB', secret_key='anE8jZd9o8p6FEj2xScdQUAY4Hjhf6jXxFsyXuSg')
client2 = Client(access_key='NB9bgKQtz4aMUqTVr8lDjFaUTD15KMjxCZCWHP6q', secret_key='nkZDYvX1pBj05MEUxBBIZcPQScxmjpxNcEaljAEh')

sellmean = 0.1
sellsigma = 0.1
sellprice = 1000

buymean = 0.1
buysigma = 0.03
buyprice = 1010

buyscount = 0
sellscount = 0
total = 0
errorcount500 = 0

buysession = client2
sellsession = client1
x = 0
try:
    while x < 1:
        x = x + 1

        if x % 2 == 0:
            buysession = client2
            sellsession = client1
        else:
            buysession = client1
            sellsession = client2

        aloginverse = np.random.lognormal(mean=sellmean, sigma=sellsigma, size=None)
        sellloginverse = aloginverse * sellprice

        amround = round(sellloginverse, 2)
        avolumne = round(((np.random.uniform(1, 10))/10000), 8)
        sellTotal = round((amround * avolumne), 8)

        print("Sell BTC  -->", amround, avolumne, sellTotal)

        sellparams = {'market': 'btcusd', 'side': 'sell', 'volume': avolumne, 'price': amround}
        rsell = sellsession.post(get_api_path('orders'), sellparams)

        status_code = 200
        print("Order Sell Page")
        if status_code == 200:
            sellscount = sellscount + 1

        bloginverse = np.random.lognormal(mean=buymean, sigma=buysigma, size=None)
        buyloginverse = bloginverse * buyprice
        bmround = round(buyloginverse, 2)

        bvolumne = round(((np.random.uniform(1, 10))/10000), 8)
        buyTotal = round((bmround * bvolumne), 8)

        time.sleep(0.2)

        print("buy  -->", bmround, bvolumne, buyTotal)

        buyparams = {'market': 'btcusd', 'side': 'buy', 'volume': bvolumne, 'price': bmround}
        rbuy = buysession.post(get_api_path('orders'), buyparams)

        print("Order Buy Page")
        if status_code == 200:
            buyscount = buyscount + 1

        total = total + 1

        if (status_code == 500) or (status_code == 500):
            errorcount500 = errorcount500 + 1

        time.sleep(0.2)

except Exception as ex:
    print("Error Occured after iteration number ",total)
finally:
    print("total --> ", total)
    print("buys --> ", buyscount)
    print("sells --> ", sellscount)
    print("500 Error Count --> ", errorcount500)

#demo of POST APIs
#DANGROUS, you better use test account to debug POST APIs

"""
markets =  client.get(get_api_path('markets'))
print(markets

#sell 10 dogecoins at price 0.01
params = {'market': 'dogcny', 'side': 'sell', 'volume': 10, 'price': 0.01}
res = client.post(get_api_path('orders'), params)
print(res

#buy 10 dogecoins at price 0.001
params = {'market': 'dogcny', 'side': 'buy', 'volume': 10, 'price': 0.001}
res = client.post(get_api_path('orders'), params)
print(res

#clear all orders in all markets
res = client.post(get_api_path('clear'))
print(res
#delete a specific order by order_id

#first, let's create an sell order
#sell 10 dogecoins at price 0.01
params = {'market': 'dogcny', 'side': 'sell', 'volume': 12, 'price': 0.01}
res = client.post(get_api_path('orders'), params)
print(res
order_id = res['id']

#delete this order
params = {"id": order_id}
res = client.post(get_api_path('delete_order'), params)
print(res

#create multi orders
params = {'market': 'dogcny', 'orders': [{'side': 'buy', 'volume': 12, 'price': 0.0002}, {'side': 'sell', 'volume': 11, 'price': 0.01}]}
res = client.post(get_api_path('multi_orders'), params)
print(res
"""
