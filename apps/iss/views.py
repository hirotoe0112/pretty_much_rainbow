from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response_json = response.json()
    context = {
        "longitude": response_json["iss_position"]["longitude"],
        "latitude": response_json["iss_position"]["latitude"],
    }
    return render(request, "iss/index.html", context)
