# quiz/forms.py
from django import forms
from .models import QuizTaker

class QuizTakerForm(forms.ModelForm):
    class Meta:
        model = QuizTaker
        fields = ['user', 'quiz', 'score']
