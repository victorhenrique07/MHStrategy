from .models import Monsters
from .forms import MonsterForm
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def home(request):
    return HttpResponse("Teste")

def monsters(request):
    try:
        api_url = "https://mhw-db.com/monsters"
        response = requests.get(api_url)
        data = response.json()
        monster_list = []
        for i in data:
            monster_list.append(i["name"])
        json_teste = json.dumps(monster_list)
        return HttpResponse(json_teste)
    except Exception as e:
        print(e)
        return HttpResponse(e)


def get_monster(request, id):
    api_url = f"https://mhw-db.com/monsters/{id}"
    response = requests.get(api_url)
    data = response.json()
    return HttpResponse(data["id"], data["name"])


def register_monster(request, id):
    try:
        form = MonsterForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                api_url = f"https://mhw-db.com/monsters/{id}"
                response = requests.get(api_url)
                data = response.json()
                json_data = json.dumps(data)
                form.save()
                form = MonsterForm()
                return HttpResponse(json_data, content_type='application/json')
    except Exception as e:
        print(e)
        return HttpResponse(e)