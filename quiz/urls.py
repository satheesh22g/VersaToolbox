from django.urls import path
from .views import quiz_list, take_quiz, create_quiz, delete_quiz, leaderboard

urlpatterns = [
    path('quizzes/', quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', take_quiz, name='take_quiz'),
    path('create_quiz/', create_quiz, name='create_quiz'),
    path('delete_quiz/<int:quiz_id>/', delete_quiz, name='delete_quiz'),
    path('leaderboard/', leaderboard, name='leaderboard'),
]
