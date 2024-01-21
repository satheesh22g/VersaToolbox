# quiz/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseServerError
from django.contrib import messages

from .models import Quiz, Question, Option, QuizTaker
from .forms import QuizTakerForm

from django.utils import timezone
from datetime import timedelta

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

@login_required
def take_quiz(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    
    last_quiz_taken_time_str = request.session.get(f'last_quiz_taken_{quiz_id}')
    if last_quiz_taken_time_str:
        last_quiz_taken_time = timezone.datetime.fromisoformat(last_quiz_taken_time_str)
        time_elapsed = timezone.now() - last_quiz_taken_time
        if time_elapsed < timedelta(days=1):
            time_remaining = timedelta(days=1) - time_elapsed
            return render(request, 'too_soon.html', {'quiz': quiz, 'time_remaining': time_remaining})
    
    if request.method == 'POST':
        score = calculate_score(request, questions)
        
        quiz_taker = QuizTaker.objects.create(
            user=request.user,
            quiz=quiz,
            score=score
        )
        
        request.session[f'last_quiz_taken_{quiz_id}'] = timezone.now().isoformat()
        
        return redirect('leaderboard')

    return render(request, 'take_quiz.html', {'quiz': quiz, 'questions': questions})

def calculate_score(request, questions):
    score = 0

    for question in questions:
        answer_key = f'question_{question.id}'
        submitted_option_id = request.POST.get(answer_key)

        try:
            correct_option_id = Option.objects.get(question=question, is_correct=True).id
            is_correct = submitted_option_id == str(correct_option_id)
        except Option.DoesNotExist:
            is_correct = False

        if is_correct:
            score += 1

    return score

def leaderboard(request):
    leaderboard = QuizTaker.objects.all().order_by('-score')
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard})


@staff_member_required
def create_quiz(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            category = request.POST.get('category')

            quiz = Quiz.objects.create(title=title, category=category)

            # Extract question data
            question_texts = request.POST.getlist('questions-text')
            options_1_list = request.POST.getlist('option-1')
            options_2_list = request.POST.getlist('option-2')
            options_3_list = request.POST.getlist('option-3')
            options_4_list = request.POST.getlist('option-4')
            correct_options_list = request.POST.getlist('correct-option')

            for question_text, option_1, option_2, option_3, option_4, correct_option in zip(
                question_texts, options_1_list, options_2_list, options_3_list, options_4_list, correct_options_list
            ):
                question = Question.objects.create(quiz=quiz, text=question_text)

                options_text = [option_1, option_2, option_3, option_4]
                correct_option_index = int(correct_option)

                for i, option_text in enumerate(options_text):
                    is_correct = i + 1 == correct_option_index
                    Option.objects.create(question=question, text=option_text, is_correct=is_correct)

            messages.success(request, "Quiz created successfully.")
            return redirect('quiz_list')
        except Exception as e:
            print(f"Error creating quiz: {e}")
            messages.error(request, "An error occurred while creating the quiz.")

    return render(request, 'create_quiz.html')


@staff_member_required
def delete_quiz(request, quiz_id):
    try:
        quiz = Quiz.objects.get(pk=quiz_id)
        quiz.delete()
        messages.success(request, "Quiz deleted successfully.")
    except Quiz.DoesNotExist:
        messages.error(request, "Quiz not found.")
    
    return redirect('quiz_list')
