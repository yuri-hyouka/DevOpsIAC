from django.shortcuts import render
import requests
import json
from googletrans import Translator

def getTraducao(texto):
    translator = Translator()
    resultado  = translator.translate(texto,dest='en')
    return resultado.text

def personagens(request):
    api_url  = f'https://last-airbender-api.fly.dev/api/v1/characters'
    response = requests.get(api_url)
    dados    = response.json()
    lista_traduzida = []

    for item in dados:
        nome      = item.get('name', 'Desconhecido')
        afiliacao = item.get('affiliation', 'Sem afiliação')
        lista_traduzida.append({
            'nome': getTraducao(nome),
            'afiliacao': getTraducao(afiliacao),
        })

    return render(request, 'Avatar/lista_traduzida.html', {'personagens': lista_traduzida})