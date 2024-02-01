from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Import the login_required decorator
from .models import Food, Consume
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from .models import Food, Consume
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from datetime import datetime
from .models import Food, Consume
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Food, Consume
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from datetime import datetime

@login_required
def c_index(request):
    if request.method == "POST":
        food_consumed_id = request.POST.get('food_consumed')
        current_date = datetime.now().date()
        
        if food_consumed_id and current_date:
            # Convert the date string to a datetime objec
            
            # Check if the food item already exists in the database
            food_item = get_object_or_404(Food, id=food_consumed_id)

            # Check if the user has already consumed this food item on the selected date
            consume_entry, created = Consume.objects.get_or_create(
                user=request.user, 
                food_consumed=food_item,
                date=current_date
            )

            # If the user has already consumed it, update the quantity
            if not created:
                consume_entry.quantity += 1.0
                consume_entry.save()

    # Retrieve all foods and consumed foods for rendering
    foods = Food.objects.all()
    
    # Retrieve the selected date from the query parameters
    selected_date_str = request.POST.get('consume_date')
    print("selected_date_str----->",selected_date_str)
    selected_date = datetime.now().date() if not selected_date_str else datetime.strptime(selected_date_str, '%Y-%m-%d').date()

    # Filter consumed food by the selected date
    consumed_food = Consume.objects.filter(user=request.user, date=selected_date)

    # Calculate the total values
    total_carbs = consumed_food.aggregate(Sum('food_consumed__carbs'))['food_consumed__carbs__sum'] or 0
    total_protein = consumed_food.aggregate(Sum('food_consumed__protein'))['food_consumed__protein__sum'] or 0
    total_fats = consumed_food.aggregate(Sum('food_consumed__fats'))['food_consumed__fats__sum'] or 0
    total_calories = consumed_food.aggregate(Sum('food_consumed__calories'))['food_consumed__calories__sum'] or 0

    context = {
        'foods': foods,
        'consumed_food': consumed_food,
        'total_carbs': total_carbs,
        'total_protein': total_protein,
        'total_fats': total_fats,
        'total_calories': total_calories,
        'selected_date': selected_date.strftime('%Y-%m-%d'),
    }

    return render(request, 'cal_index.html', context)
 

@login_required  # Use the login_required decorator for views that require authentication
def delete_consume(request, id):
    try:
        consumed_food = Consume.objects.get(id=id)
    except Consume.DoesNotExist:
        return redirect('/')  # Redirect to a suitable page if the object doesn't exist

    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    
    return render(request, 'delete.html')
