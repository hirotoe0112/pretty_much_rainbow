from django.shortcuts import render
from django.template import loader
from django.contrib.staticfiles import finders
import random
import pandas

def get_yojijukugo():
    csv_file_path = finders.find("index/yojijukugo.csv")
    csv_data = pandas.read_csv(csv_file_path)
    dict_data = csv_data.to_dict(orient="records")
    return random.choice(dict_data)



# Create your views here.
def index(request):
    context = {
        "fc": get_yojijukugo(),
    }
    return render(request, "index/index.html", context)
