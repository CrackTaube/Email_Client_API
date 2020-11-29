from requests import Request, Session
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


def open(file: "json_data.txt",mood: 'r') as f:
    data = json.loads(data_sheet)


print(data)

'''
data = json.loads(response.text)
data_price_now = data['EUR']['price']
print(json.dumps(data, indent=4, sort_keys=True))  #Makes the Json Readable
print(data_price_now)
'''