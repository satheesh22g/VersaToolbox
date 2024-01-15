# quiz/urls.py
from django.urls import path
from .views import quiz_list, take_quiz, leaderboard

urlpatterns = [
    path('quizzes/', quiz_list, name='quiz_list'),
    path('quizzes/<int:quiz_id>/take/', take_quiz, name='take_quiz'),
    path('quizzes/leaderboard/', leaderboard, name='leaderboard'),
]
