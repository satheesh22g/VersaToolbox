from django.shortcuts import render, redirect
from django.views import View
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse



@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expense_list.html', {'expenses': expenses})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})


@login_required
def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    redirect_url = reverse('expense_list')
    return JsonResponse({'message': 'Expense deleted successfully', 'redirect_url': redirect_url})



