import requests

API_KEY = "fca_live_s7yfZVmd926QVftbCbK2TyQZMYlOsxHg7VE8cpFZ"

BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "AUD", "CAD", "CNY","INR"]




def convert_currency(base):
    currency_separated_by_comma = ",".join(CURRENCIES)   
    url = f"{BASE_URL}&base_currency={base}&currencies={currency_separated_by_comma}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if status code is 4xx or 5xx
        data = response.json()
        return data['data']
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
    except ValueError:
        print("Response content is not valid JSON.")
    except KeyError:
        print("Expected 'data' key is missing in the JSON response.")
    # try:
    #     response = requests.get(url)
    #     data = response.json()
    #     print(data)
    #     # print(data) because the json body has the currencies inside the data array
    #     return data['data']
    # except:
    #     print(f"Invalid input")
    #     return None

def format_data(data):
    # print(data.items())
    for curr,value in data.items():
        print(f"{curr} : {value} ")

while True:
    base = input("input your base currency (press q to quit):  ").upper()
    if base == "Q": # capital Q is okay here since we are already convertiong the input to upper case. 
        #the other reason is in "nuances" file in obsedian
        break
    data = convert_currency(base)
    if not data: # if the data is not a falsy [check obsedian notes]
        continue
    format_data(data)
        


