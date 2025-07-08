from django.shortcuts import render
import requests
from googletrans import Translator

def getTraducao(texto):
    translator = Translator()
    resultado = translator.translate(texto, dest='pt')
    return resultado.text

def personagens(request):
    pagina = int(request.GET.get('page', 1))
    limite = 10
    offset = (pagina - 1) * limite

    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters?perPage={limite}&page={pagina}'
    response = requests.get(api_url)

    if response.status_code != 200:
        return render(request, 'Avatar/lista_traduzida.html', {
            'personagens': [],
            'pagina': pagina,
            'tem_mais': False,
            'erro': 'Erro ao acessar a API externa.'
        })

    dados = response.json()
    lista_traduzida = []

    for item in dados:
        nome = item.get('name', 'Desconhecido')
        afiliacao = item.get('affiliation', 'Sem afiliação')
        foto = item.get('photoUrl')
        lista_traduzida.append({
            'nome': getTraducao(nome),
            'afiliacao': getTraducao(afiliacao),
            'foto': foto
        })

    # Verifica se há mais personagens na próxima página
    tem_mais = len(dados) == limite

    # Número de páginas visíveis
    total_paginas = list(range(1, pagina + 3))

    return render(request, 'Avatar/lista_traduzida.html', {
        'personagens': lista_traduzida,
        'pagina': pagina,
        'tem_mais': tem_mais,
        'offset': offset,
        'total_paginas': total_paginas
    })
