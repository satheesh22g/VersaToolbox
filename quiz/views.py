# quiz/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Option, QuizTaker
from .forms import QuizTakerForm
# quiz/views.py
from django.utils import timezone
from datetime import timedelta
from .models import Quiz, Question, Option, QuizTaker
from .forms import QuizTakerForm


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

@login_required
def take_quiz(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    
    # Check if the user has already taken this quiz within a day
    last_quiz_taken_time_str = request.session.get(f'last_quiz_taken_{quiz_id}')
    if last_quiz_taken_time_str:
        last_quiz_taken_time = timezone.datetime.fromisoformat(last_quiz_taken_time_str)
        time_elapsed = timezone.now() - last_quiz_taken_time
        if time_elapsed < timedelta(days=1):
            time_remaining = timedelta(days=1) - time_elapsed
            return render(request, 'too_soon.html', {'quiz': quiz, 'time_remaining': time_remaining})
    
    if request.method == 'POST':
        # Process submitted answers
        score = calculate_score(request, questions)
        
        # Save the QuizTaker instance
        quiz_taker = QuizTaker.objects.create(
            user=request.user,
            quiz=quiz,
            score=score
        )
        
        # Update the last quiz taken time in the session
        request.session[f'last_quiz_taken_{quiz_id}'] = timezone.now().isoformat()
        
        # Redirect to the leaderboard
        return redirect('leaderboard')

    return render(request, 'take_quiz.html', {'quiz': quiz, 'questions': questions})

def calculate_score(request, questions):
    score = 0

    for question in questions:
        # Get the submitted answer for each question
        answer_key = f'question_{question.id}'
        submitted_option_id = request.POST.get(answer_key)

        # Check if the submitted option is correct
        correct_option_id = Option.objects.get(question=question, is_correct=True).id
        is_correct = submitted_option_id == str(correct_option_id)

        # Increment the score for correct answers
        if is_correct:
            score += 1

    return score
def leaderboard(request):
    leaderboard = QuizTaker.objects.all().order_by('-score')
    return render(request, 'leaderboard.html', { 'leaderboard': leaderboard})
