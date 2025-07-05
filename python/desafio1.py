import requests
import json

def getPersonagens():
    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters'
    response = requests.get(api_url)
    print(response.status_code)
    print(response.headers)
    #print(response.json())
    print(json.dumps(response.json(), indent=4))

getPersonagens()