from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    upperCharacters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    symbols = list('!"#$%&')
    length = 10
    password = ''

    for x in range(length):
        password+=random.choice(characters)

    return render(request, 'generator/password.html', {'password':password})
