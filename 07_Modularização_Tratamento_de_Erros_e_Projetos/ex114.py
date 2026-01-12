import requests

url = "https://pudim@pudim.com.br"
try:
    resposta = requests.get(url, timeout=3)
    if resposta.status_code == 200:
        print('Site Acessível')
    else:
        print(f'Site respondeu, mas com status {resposta.status_code}')
except requests.exceptions.RequestException:
    print('Site incessível ou erro de conexão')