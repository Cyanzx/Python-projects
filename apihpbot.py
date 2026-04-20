import requests
import pprint

url = 'https://harry-potter-open-api-ff4c7a51ed23.herokuapp.com/api/v1/creatures/'

resposta = requests.get(url)
creaturas = resposta.json()

pprint.pprint(creaturas)

