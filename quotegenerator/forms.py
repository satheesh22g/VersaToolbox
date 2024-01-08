# quotegenerator/forms.py
from django import forms

class WordsForm(forms.Form):
    words = forms.CharField(label='Enter words (comma-separated)', max_length=200)
