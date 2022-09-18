from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    upperCharacters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    digits = list('123456789')
    symbols = list('!"#$%&')
    length = int(request.GET.get('length', 1))
    password = ''

    if request.GET.get('uppercase'):
        characters.extend(upperCharacters)

    if request.GET.get('digits'):
        characters.extend(digits)

    if request.GET.get('special_symbols'):
        characters.extend(symbols)

    for x in range(length):
        password+=random.choice(characters)

    return render(request, 'generator/password.html', {'password':password})
