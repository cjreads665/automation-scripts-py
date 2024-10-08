import requests

API_KEY = "fca_live_s7yfZVmd926QVftbCbK2TyQZMYlOsxHg7VE8cpFZ"

BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "AUD", "CAD", "CNY","INR"]

base = input("input your base currency (press q to quit):  ").upper()


def convert_currency(base):
    currency_separated_by_comma = ",".join(CURRENCIES)   
    url = f"{BASE_URL}&base_currency={base}&currencies={currency_separated_by_comma}"
    try:
        response = requests.get(url)
        data = response.json()
        # print(data)
        return data['data']
    except:
        print(f"some error occured with message: {e}")
        return None

def format_data(data):
    print(data.items())
    for curr,value in data.items():
        print(f"{curr} : {value} ")

while True:
        format_data(convert_currency(base))
        break

        


