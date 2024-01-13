# urls.py

from django.urls import path
from .views import expense_list, add_expense, delete_expense

urlpatterns = [
    path('expenses/', expense_list, name='expense_list'),
    path('add_expense/', add_expense, name='add_expense'),
    path('delete_expense/<int:expense_id>/', delete_expense, name='delete_expense'),
]
