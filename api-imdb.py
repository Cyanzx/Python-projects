import requests

api = 'https://imdbapi.dev/'

resposta = requests.get(api)
dados = resposta.json()

print(dados)