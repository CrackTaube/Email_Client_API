from requests import Request, Session
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start':'1',
    'limit':'2',
    'convert':'EUR',
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '5265337e-58a3-4d61-9e41-2bdb9f24f828',
}

session = Session()
btc_price_now = []
session.headers.update(headers)
response = session.get(url, params=parameters)
data = json.loads(response.text)


def btc_price():
    data_list = data['data']
    data_dict1 = data_list[0]
    data_dict2 = data_dict1['quote']
    euro_dict = data_dict2['EUR']
    btc_price_now.append(euro_dict['price'])
    btc_price_now.append(euro_dict['percent_change_1h'])
    btc_price_now.append(euro_dict['percent_change_24h'])
    btc_price_now.append(euro_dict['percent_change_7d'])

btc_price()

print(btc_price_now)

'''
try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    #print(json.dumps(data, indent=4, sort_keys=True))  #Makes the Json Readable
    data_test = data['data']
    data_1 = data_test[0]
    data_2 = data_1['quote']
    data_3 = data_2['EUR']
    data_price = data_3['price']
    data_1h = data_3['percent_change_1h']
    data_24h = data_3['percent_change_24h']
    data_7d = data_3['percent_change_7d']
    
    print(data_price)
    print(data_1h)
    print(data_24h)
    print(data_7d)
    print(type(data_test))
    #print(data)

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)




def get_latest_crypto_price(crypto):
  
  response = requests.get(TICKER_API_URL+crypto)
  response_json = response.json()
  
  return float(response_json[0]['price_eur'])

get_latest_crypto_price('bitcoin')


'''