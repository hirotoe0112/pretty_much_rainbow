from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    context = {
        "version": "1.0.0",
    }
    return render(request, "index/index.html", context)
