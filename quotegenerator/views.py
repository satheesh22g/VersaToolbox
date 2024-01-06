from django.shortcuts import render
import requests
from .forms import WordsForm

def fetch_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        data = response.json()
        quote = data['content']
        author = data['author']
        return quote, author
    return "No quote available at the moment.", "Unknown"

def generate_quote(request):
    if request.method == 'POST':
        random_quote, author = fetch_quote()
        return render(request, 'quote.html', {'quote': random_quote, 'author': author})

    return render(request, 'generate_quote.html')
