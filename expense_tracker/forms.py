# forms.py

from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'date', 'category', 'description']

    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
    }
