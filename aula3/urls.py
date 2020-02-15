from django.urls import path
from .views import index,setCookie,redirect


app_name = "aula3"

'''
    Aqui criamos uma rota para acessar as imagens dentro do document root
se colocar a barra o mesmo chama o diretorio passando o mesmo, sem ele é passado
que o mesmo faz referencia ao init 
'''

urlpatterns = [
    path('', index),
    path('cookie', setCookie),
    path('uol', redirect),
]
