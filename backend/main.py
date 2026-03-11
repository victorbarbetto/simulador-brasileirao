from settings import API_TOKEN
import requests

url = 'https://api.football-data.org//v4/teams/1779/matches'

headers = {
    'X-Auth-Token': API_TOKEN
}

resposta = requests.get(url, headers=headers)

print(resposta.status_code)
print(resposta.json())
