import requests

TOKEN = '798979267:AAEWbRlo36GcdtkvhM7AQ8psNpnx041nWUk'
MAIN_URL = f'https://api.telegram.org/bot/{TOKEN}'

r = requests.get(f'{MAIN_URL}/getMe')

print(r.json())












