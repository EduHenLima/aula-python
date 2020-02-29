from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "alunos":[
            "Joao",
            "Maria",
            "Jose",
            "Pedro",
        ]
    }
    return render(request, 'aula4/index.html', context=context)
