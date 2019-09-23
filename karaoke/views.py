from django.shortcuts import render

# Create your views here.
def index(request): 
    context={
        'minhavar':[
            'eric',
            'bruno',
            'camila'
        ]
    }
    return render (request, "index.html", context) #recebe a requição e devolve o template index