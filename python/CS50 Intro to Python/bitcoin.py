import sys
import requests
import json



try:
    num_btc = float(sys.argv[1])
except ValueError:
    sys.exit("Please enter a number as argument.")

btc_rate = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=cee6935c6f20227aa6a217d6d28944f3a584222d8670887a1252a3beddfda404")
#json.dumps(btc_rate.json(), indent=4))
response = btc_rate.json()
price_usd = float(response.get("data").get("priceUsd"))
total_price = price_usd * num_btc

print(f"Price of Bitcoin is ${total_price:,.4f}")


