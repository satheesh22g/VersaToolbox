from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

from .models import Question, Quiz, QuizTaker


class QuizRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.__name__ == "take_quiz" and request.method == "GET":
            quiz_id = view_kwargs.get("quiz_id")
            if quiz_id:
                quiz = Quiz.objects.get(pk=quiz_id)
                user = request.user

                # Check if the user has already achieved a perfect score in this quiz
                perfect_score_taker = QuizTaker.objects.filter(
                    user=user,
                    quiz=quiz,
                    score=Question.objects.filter(quiz=quiz).count(),
                ).first()

                if perfect_score_taker:
                    last_perfect_score_time_str = request.session.get(
                        f"last_perfect_score_time_{quiz_id}"
                    )
                    if last_perfect_score_time_str:
                        last_perfect_score_time = timezone.datetime.fromisoformat(
                            last_perfect_score_time_str
                        )
                        time_elapsed = timezone.now() - last_perfect_score_time
                        cooldown_period = timedelta(days=7)

                        if time_elapsed < cooldown_period:
                            return render(
                                request,
                                "quiz_restriction.html",
                                {"cooldown_period": cooldown_period},
                            )

        return None
