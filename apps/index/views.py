from django.shortcuts import render
from django.template import loader
import datetime as dt

function_list = {
    "2024_06": [
        {
            "name": "機能A",
            "done": True,
        },
        {
            "name": "機能B",
            "done": False,
        },
        {
            "name": "機能#",
            "done": False,
        },
    ],
    "2024_07": [],
}


# Create your views here.
def index(request):
    current_ym = dt.datetime.now().strftime("%Y_%m")
    functions = function_list[current_ym]
    # done=Trueのものをカウント
    done_count = sum(1 for function in functions if function["done"])
    # 進捗率
    progress = round(done_count / len(functions) * 100, 1)
    context = {
        "version": "1.0.0",
        "progress_name": f"function_{current_ym}",
        "progress": progress,
    }
    return render(request, "index/index.html", context)
