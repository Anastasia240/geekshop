from django.urls import path
from mainapp.views import login

urlpatterns = [
    path('login', login, name="login"),

]
