from django import forms
from django.forms.widgets import NumberInput
from django.forms.fields import DateField
from .models import Document

class QRForm(forms.Form):
    url = forms.CharField(label="Enter URL", max_length=100)
    url.widget.attrs.update({'class' : 'input-field'})

class YtMp3Form(forms.Form):
    url = forms.CharField(label="Enter URL", max_length=100)
    url.widget.attrs.update({'class' : 'input-field'})

class MobileForm(forms.Form):
    number = forms.IntegerField()
    number.widget.attrs.update({'class' : 'input-field'})
class ZodiacForm(forms.Form):
    date_input = forms.DateTimeField(label="Enter Your DOB", required=True, widget=NumberInput(attrs={'type':'date'}))

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('pdf_file',)