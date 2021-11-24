import json

import requests
enter = 'USD'
exits = 'UZS'
# Where USD is the base currency you want to use
url = f'https://v6.exchangerate-api.com/v6/f4c3988ec1b2915571fc66f8/pair/{enter}/{exits}'

# Making our request
response = requests.get(url)
data = response.json()



