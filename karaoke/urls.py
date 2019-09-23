from django.urls import path
from . import views #importando o arquivo views.py

urlpatterns = [
    path('', views.index, name='Index') #linha para receber a requisição e devolver o index
]