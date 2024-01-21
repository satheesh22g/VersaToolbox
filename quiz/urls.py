from django.urls import path
from .views import quiz_list, take_quiz, create_quiz, delete_quiz, leaderboard, user_scores  # Import user_scores

urlpatterns = [
    path('quizzes/', quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', take_quiz, name='take_quiz'),
    path('create_quiz/', create_quiz, name='create_quiz'),
    path('delete_quiz/<int:quiz_id>/', delete_quiz, name='delete_quiz'),
    path('leaderboard/', leaderboard, name='leaderboard'),
    path('user_scores/<str:username>/', user_scores, name='user_scores'),

]
