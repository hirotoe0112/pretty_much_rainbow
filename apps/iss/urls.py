from django.urls import path
from . import views

app_name = "iss"

urlpatterns = [path("", views.index, name="index")]
