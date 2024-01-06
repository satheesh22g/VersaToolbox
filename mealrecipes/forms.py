from django import forms

class RecipeForm(forms.Form):
    ingredients = forms.CharField(label='Enter Ingredients', widget=forms.TextInput(attrs={'placeholder': 'Enter ingredients separated by commas'}))
