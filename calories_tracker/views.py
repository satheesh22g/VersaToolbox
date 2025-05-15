from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .models import Consume, Food


@login_required
def c_index(request):
    # Default to today's date or get selected date from POST
    selected_date_str = request.POST.get("consume_date")
    selected_date = (
        datetime.now().date()
        if not selected_date_str
        else datetime.strptime(selected_date_str, "%Y-%m-%d").date()
    )

    if request.method == "POST":
        food_consumed_id = request.POST.get("food_consumed")
        if food_consumed_id:
            food_item = get_object_or_404(Food, id=food_consumed_id)

            # Track or update consumption for this user/date/food
            consume_entry, created = Consume.objects.get_or_create(
                user=request.user, food_consumed=food_item, date=selected_date
            )
            if not created:
                consume_entry.quantity += 1.0
                consume_entry.save()

    # Fetch all foods and this user's consumed foods for the selected date
    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user, date=selected_date)

    # Aggregate totals
    aggregates = consumed_food.aggregate(
        total_carbs=Sum("food_consumed__carbs"),
        total_protein=Sum("food_consumed__protein"),
        total_fats=Sum("food_consumed__fats"),
        total_calories=Sum("food_consumed__calories"),
    )

    # Ensure None values are converted to 0
    totals = {key: value or 0 for key, value in aggregates.items()}

    context = {
        "foods": foods,
        "consumed_food": consumed_food,
        "selected_date": selected_date.strftime("%Y-%m-%d"),
        **totals,
    }

    return render(request, "cal_index.html", context)


@login_required
def delete_consume(request, id):
    consumed_food = get_object_or_404(Consume, id=id)

    if request.method == "POST":
        consumed_food.delete()
        return redirect("/")

    return render(request, "delete.html")
