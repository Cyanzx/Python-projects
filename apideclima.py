import requests
import pprint

api_key = 'token'

url = 'http://api.weatherapi.com/v1/current.json'

#cria-se um dicionario para passar os parametros
while True: 

    cidade = input("Qual a cidade: ")
    if cidade == "sair":
        break
    
    parametros = {
    "key" : api_key,
    "q" : cidade,
    "lang": "pt",
}

    resposta = requests.get(url, params=parametros)

# print(resposta)
# print(resposta.content)

    if resposta.status_code == 200:
        dados_requisicao = resposta.json()
    # pprint.pprint(dados_requisicao) aqui mostra todas as informações em formato de dicionario
        temp = dados_requisicao["current"]["temp_c"]
        desc = dados_requisicao["current"]["condition"]["text"]
        print(temp, desc)