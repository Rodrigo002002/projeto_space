from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Project Space</h1><p>Bem vindo ao espaço</p>')