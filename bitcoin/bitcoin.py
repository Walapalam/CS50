import requests
import sys
import json

def get_bitcoinNum():
    bitcoin_amount = sys.argv[1]
    try:
        float(bitcoin_amount)
    except:
        sys.exit("Invalid Input")
    return float(bitcoin_amount)

def get_input():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()

    list = response["bpi"]
    USD = list["USD"]
    USD_float = USD["rate_float"]
    return float(USD_float)

def main():
    NoOfCoins = get_bitcoinNum()
    rate = get_input()
    amount = NoOfCoins * rate

    print(f"Amount: ${amount:,.4f}")

main()
