import requests
import json
from googletrans import Translator

def getTraducao(texto):
    translator = Translator()
    resultado  = translator.translate(texto,dest='en')
    return resultado.text

def getPersonagens():
    api_url  = f'https://last-airbender-api.fly.dev/api/v1/characters'
    response = requests.get(api_url)
    dados    = response.json()

    for item in dados:
        nome      = item.get('name', 'Desconhecido')
        afiliacao = item.get('affiliation', 'Sem afiliação')
        print('Nome: ', getTraducao(nome))
        print('Afiliação: ', getTraducao(afiliacao))
        print(' ')

getPersonagens()










#resultado = translator.translate("Olá, tudo bem?", src='pt', dest='en')
#print(resultado.text)
#print(response.status_code)
#print(response.headers)
#print(response.json())
#print(json.dumps(response.json(), indent=4))