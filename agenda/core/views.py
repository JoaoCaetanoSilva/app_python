from django.shortcuts import render

def lista_eventos(request):
    render(request, 'agenda.html')