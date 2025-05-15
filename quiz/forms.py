# quiz/forms.py
from django import forms

from .models import Quiz, QuizTaker


class QuizTakerForm(forms.ModelForm):
    class Meta:
        model = QuizTaker
        fields = ["user", "quiz", "score"]


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            "title",
            "category",
        ]  # Add any other fields you want to include in the form
