from django.urls import path
from . import views

app_name = "words"

urlpatterns = [path("", views.index, name="index")]
