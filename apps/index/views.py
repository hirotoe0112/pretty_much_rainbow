from django.shortcuts import render
from django.template import loader
import random

fc_list = [
    {
        "name": "四面楚歌",
        "meaning": "四面楚歌，形容处境危险，四面受敌。出自《史记·项羽本纪》。",
    },
    {
        "name": "五里霧中",
        "meaning": "形容事物模糊不清，不易看清。出自《史记·平原君虞卿列传》。",
    },
]


# Create your views here.
def index(request):
    context = {
        "fc": random.choice(fc_list),
    }
    return render(request, "index/index.html", context)
