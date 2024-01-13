from .models import Quote  # Import your Quote model
from django.shortcuts import render


def fetch_quote():
    try:
        # Fetch a random quote from the database
        quote = Quote.objects.order_by('?').first()

        if quote:
            return quote.content, quote.author
        else:
            return "No quote available at the moment.", "Unknown"

    except Exception as e:
        print(f"Error fetching quote from database: {e}")
        return "No quote available at the moment.", "Unknown"
    
def generate_quote(request):
    if request.method == 'POST':
        random_quote, author = fetch_quote()
        return render(request, 'quote.html', {'quote': random_quote, 'author': author})

    return render(request, 'generate_quote.html')


















# from django.shortcuts import render
# import requests

# def fetch_quote():
#     try:
#         response = requests.get('https://api.quotable.io/random')
#         response.raise_for_status()  # Raise HTTPError for bad responses
#         data = response.json()
#         quote = data['content']
#         author = data['author']
#         return quote, author
#     except requests.RequestException as e:
#         print(f"Error fetching quote: {e}")
#         return "No quote available at the moment.", "Unknown"


# def generate_quote(request):
#     if request.method == 'POST':
#         random_quote, author = fetch_quote()
#         return render(request, 'quote.html', {'quote': random_quote, 'author': author})

#     return render(request, 'generate_quote.html')
