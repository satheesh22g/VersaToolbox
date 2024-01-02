# quotegenerator/views.py
from django.shortcuts import render
import requests
from .forms import WordsForm

def fetch_quote():
    response = requests.get('https://zenquotes.io/api/random')
    data = response.json()
    if data:
        quote = data[0]['q']
        author = data[0]['a']
        return quote,author
    return "No quote available at the moment."

def generate_quote(request):
    if request.method == 'POST':
        random_quote, author = fetch_quote()
        return render(request, 'quote.html', {'quote': random_quote,'author':author})

    return render(request, 'generate_quote.html')
