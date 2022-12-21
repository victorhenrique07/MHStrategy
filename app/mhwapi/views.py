from .forms import MonsterForm
from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home(request):
    return HttpResponse("Teste")

def monsters(request):
    api_url = "https://mhw-db.com/monsters"
    response = requests.get(api_url)
    response.json()
    data = []
    for i in response:
        data.append(i["name"])
    return HttpResponse(response)

def monsters(request):
    import json
    with open('mhwapi/monsters.json', encoding='utf-8') as monsters_json:
        data = json.load(monsters_json)
        
    item = []
    for i in data:
        item.append(i["name"])
    data = json.dumps(item)
    return HttpResponse(item)