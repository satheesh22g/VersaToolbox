# quiz/middleware.py
from django.utils import timezone
from datetime import timedelta
from .models import Quiz, Question, Option, QuizTaker
from django.shortcuts import render, redirect

# quiz/middleware.py
from django.utils import timezone
from datetime import timedelta
from .models import QuizTaker

class QuizRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.__name__ == 'take_quiz' and request.method == 'GET':
            quiz_id = view_kwargs.get('quiz_id')
            if quiz_id:
                quiz = Quiz.objects.get(pk=quiz_id)
                user = request.user

                # Check if the user has already achieved a perfect score in this quiz
                perfect_score_taker = QuizTaker.objects.filter(
                    user=user,
                    quiz=quiz,
                    score=len(Question.objects.filter(quiz=quiz))
                ).first()

                if perfect_score_taker:
                    # Check if enough time has passed since the last perfect score
                    last_perfect_score_time_str = request.session.get(f'last_perfect_score_time_{quiz_id}')
                    if last_perfect_score_time_str:
                        last_perfect_score_time = timezone.datetime.fromisoformat(last_perfect_score_time_str)
                        time_elapsed = timezone.now() - last_perfect_score_time
                        cooldown_period = timedelta(days=7)  # You can adjust the cooldown period

                        if time_elapsed < cooldown_period:
                            # If within the cooldown period, redirect to a page indicating the restriction
                            return render(request, 'quiz_restriction.html', {'cooldown_period': cooldown_period})

        return None
