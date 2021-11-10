from django.shortcuts import render

def sobre_request(request):
    return render(request, 'sobre/sobre.html')