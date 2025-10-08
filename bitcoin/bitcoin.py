
# Bitcoin Price Index
# Andrew Waddington

import json
import requests
import sys
try:
    if len(sys.argv) < 2:
        sys.exit("You gotta throw me a bone")
    my_string = float(sys.argv[1])
except ValueError:
    sys.exit("problem")
except IndexError:
    sys.exit("Yaaaar")


print (f"{my_string} \n")


response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
#content = json.dumps(response.json(), indent=2)
#content = json.loads(response.json())
#print (content)

c_dict = json.loads(json.dumps(response.json()))
#print (c_dict)

print (f"{c_dict['data']['priceUsd']}")

BTC_price = float(f"{c_dict['data']['priceUsd']}")
#BTC_price = str(BTC_price).strip()
#BTC_price = float(BTC_price)

#print (BTC_price)
print(f"${BTC_price:,.4f}")

your_coin = BTC_price * my_string
print (your_coin)
print(f"${your_coin:,.4f}")
#'priceUsd'

"""
try:
    ...
except requests.RequestException:
    sys.exit()

"""
