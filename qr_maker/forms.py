from django import forms


class NameForm(forms.Form):
    url = forms.CharField(label="Enter URL", max_length=100)