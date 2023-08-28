from django import forms


class QRForm(forms.Form):
    url = forms.CharField(label="Enter URL", max_length=100)
    url.widget.attrs.update({'class' : 'input-field'})

class YtMp3Form(forms.Form):
    url = forms.CharField(label="Enter URL", max_length=100)
    url.widget.attrs.update({'class' : 'input-field'})

class MobileForm(forms.Form):
    number = forms.IntegerField()
    number.widget.attrs.update({'class' : 'input-field'})